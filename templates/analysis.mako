<%inherit file="songbase.mako"/>

<%!
import json
%>
<%block name="extra_head">
  ${parent.extra_head()}
    <script src="/static/js/jquery-ui.js"></script>
    <link rel="stylesheet" href="/static/css/smoothness/jquery-ui-1.10.1.custom.min.css"/>

    <script>
    $(function() {
      // Load augnotes data
      window.augnotes = {
        %for key, value in augdata.items():
          ${key}:new AugmentedNotes(${json.dumps(value)}),
        %endfor
      };
      // Initialize augnotes popups
      window.media_popups = {};
      $('.augnote-popup').each(function() {
        var self=$(this);
        var dset=self.attr("data-dset");
        window.media_popups[dset] = self;
        self.dialog({
          autoOpen:false,
          modal:true,
          width:"450px",
          beforeClose: function(event, ui) {
            self.data("augnotes-ui").pause();
            self.data("augnotes-ui").setCurrentTime(0);
          },
          create: function(event, ui) {
            var score_div = self.find(".score-div");
            var audio_elt = self.find("audio.audio");
            var augnotes_ui = new AugmentedNotesUI(augnotes[dset], score_div, audio_elt);
            self.data("augnotes-ui", augnotes_ui);
          },
          open: function(event, ui) {
            self.data("augnotes-ui").play();
          }
        });
      })
      $('.snippet-popup').each(function() {
        var self=$(this);
        var dset=self.attr("data-dset");
        window.media_popups[dset] = self;
        self.dialog({
          autoOpen:false,
          modal:true,
          width:"450px",
          beforeClose: function(event, ui) {
            self.data("audio_elt")[0].pause();
            self.data("audio_elt")[0].currentTime = 0;
          },
          create: function(event, ui) {
            // clone to get around mobile safari display bug?
            var audio_elt = self.find("audio.audio").clone();
            self.find("audio.audio").replaceWith(audio_elt);
            self.data("audio_elt", audio_elt);
          },
          open: function(event, ui) {
            self.data("audio_elt")[0].play();
          }
        });
      })
    })
    function show_augnote(name, title) {
      window.media_popups[name].dialog("option", "title", title).dialog("open");
    }
    function play_snippet(name, title) {
      window.media_popups[name].dialog("option", "title", title).dialog("open");
    }
    </script>
</%block>

<%block name="title">${raw_title}</%block>

<%block name="content">
  <div class="article">
    <h2 class="title">${thetitle}</h2>

    <div style="display:none">
      %for key in augdata:
      <div class="augnote-popup" data-dset="${key}" style="display:none">
        <div class="centered" style="width:400px">
          <div class="audtools">
            <audio style="width:400px" controls="controls" class='audio' preload='auto'>
              <source id="mp3" src="/data/${key}/music.mp3" type="audio/mp3"/>
              <source id="ogg" src="/data/${key}/music.ogg" type="audio/ogg"/>
              Your browser does not support the audio tag!
            </audio>
          </div>
          <div class="score-div">
            <div class="score-page">
              <img class="score" src="/data/${key}/pages/1.jpg" width="400px" alt="Score Image"/>
            </div>
          </div>
        </div>
      </div>
      %endfor
      %for snippet in snippets:
      <div class="snippet-popup" data-dset="${snippet}" style="display:none">
        <div class="centered" style="width:400px">
          <audio style="width:400px; margin:auto" controls="controls" class='audio' preload='auto'>
            <source id="mp3" src="/data/${snippet}/music.mp3" type="audio/mp3"/>
            <source id="ogg" src="/data/${snippet}/music.ogg" type="audio/ogg"/>
            Your browser does not support the audio tag!
          </audio>
        </div>
      </div>
      %endfor
    </div>

    ${analysis_html}

  </div>
</%block>