//http://stackoverflow.com/questions/10478649/get-actual-image-size-after-resizing-it
function getImageDimensions(path,callback){
    var img = new Image();
    img.onload = function(){
        callback({
            width : img.width,
            height : img.height
        });
    }
    img.src = path;
}

function AugmentedNotesUI(augnotes, image_elt, audio_elt) {
    this.augnotes = augnotes;
    this.image_elt = $(image_elt);
    this.audio_elt = audio_elt;
    this.wrapper = $('<div style="position:relative"></div>');
    this.image_elt.parent().prepend(this.wrapper);
    var self = this;
    this.audio_elt.on("timeupdate", function() {
        self.highlightCurrentTime(this.currentTime);
    })
    var music_url = this.augnotes.getMusicUrl();
    // this.audio_elt.attr("src", music_url)
    // Before the first page is loaded, the image height is 0 and our
    // calculations for the scale factor break.
    // So we load the first page, and then when it announces that it has
    // loaded we set the current time.
    this.current_measure_id = new MeasureID(null,null);
    this.show_page(0);
    this.image_elt.one("load", function() {
        self.highlightCurrentTime();
    })
}

AugmentedNotesUI.prototype.highlightMeasure = function(measure_id) {
    var old_id = this.current_measure_id;
    this.show_page(measure_id.page_num);
    this.wrapper.find(".box").hide().eq(measure_id.measure_num).show();
    this.current_measure_id = measure_id;
    if (old_id.measure_num !== this.current_measure_id.measure_num) {
        $(this).trigger("AugmentedNotesUI-measure_change");
    }
    if (old_id.page_num !== this.current_measure_id.page_num) {
        $(this).trigger("AugmentedNotesUI-page_change");
    }
}

AugmentedNotesUI.prototype.highlightTime = function(time) {
    var measure_id = this.augnotes.measureIDAtTime(time)
    this.highlightMeasure(measure_id)
}

AugmentedNotesUI.prototype.highlightCurrentTime = function() {
    this.highlightTime(this.currentTime())
}

AugmentedNotesUI.prototype.show_page = function(num) {
    var self = this;
    var page_num = this.augnotes.clampPageNum(num);
    if (page_num === this.curr_page) return
    var path_to_img = this.augnotes.getPageUrl(page_num)
    this.image_elt.attr("src", path_to_img);
    getImageDimensions(path_to_img, function(data) {
        var original_image_w = data.width;
        var original_image_h = data.height;
        var imgw = self.image_elt.width()*1.0;
        var imgh = self.image_elt.height()*1.0;
        //scales coordinates for box image
        var width_scale = imgw/original_image_w;
        var height_scale = imgh/original_image_h;
        self.wrapper.empty();
        for (var i = 0; i < self.augnotes.getNumMeasures(page_num); i++) {
            var measure_id = new MeasureID(page_num, i);
            var measure = self.augnotes.getMeasure(measure_id);
            var box = $('<div class="box"></div>');
            box.css({
                display: "none",
                left: measure.x*width_scale + "px",
                top: measure.y*height_scale + "px",
                width: measure.w*width_scale + "px",
                height: measure.h*height_scale + "px"
            });
            self.wrapper.append(box);
        }
        self.curr_page = page_num;
    })
}

AugmentedNotesUI.prototype.currentMeasureID = function() {
    var currentTime = this.currentTime();
    return this.augnotes.measureIDAtTime(currentTime);
}

AugmentedNotesUI.prototype.currentPageNum = function() {
    return this.currentMeasureID().page_num;
}

AugmentedNotesUI.prototype.currentMeasureNum = function() {
    return this.currentMeasureID().measure_num;
}

AugmentedNotesUI.prototype.currentTime = function() {
    return this.audio_elt[0].currentTime;
}

AugmentedNotesUI.prototype.setCurrentTime = function(time) {
    this.audio_elt[0].currentTime = time;
    this.highlightCurrentTime();
}

AugmentedNotesUI.prototype.goToNextMeasure = function() {
    var page_num = this.currentPageNum();
    var m_num = this.currentMeasureNum();
    var end_time = this.augnotes.getMeasure(this.currentMeasureID()).end;
    this.setCurrentTime(end_time+.001);
}

AugmentedNotesUI.prototype.goToPrevMeasure = function() {
    var page_num = this.currentPageNum();
    var m_num = this.currentMeasureNum();
    var measure_id = this.currentMeasureID();
    if (m_num === 0 && page_num === 0) {
        var start_time = 0;
    } else {
        var prev_id = this.augnotes.getPrevMeasureID(measure_id);
        var start_time = this.augnotes.getMeasure(prev_id).start;
    }
    this.setCurrentTime(start_time+.001);
}