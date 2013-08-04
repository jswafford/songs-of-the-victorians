#!/usr/bin/env python
'''Pre-crop images based on measure data.

Given a data dir bar in dir foo with a segments.js, call:
python precropper.py all_crops foo/bar

This will create foo/bar_A, foo/bar_B, etc.

'''
import json
import copy
import os

import Image, ImageDraw, ImageTk
from consolation.app import Console

app = Console("precropper")

def absdir(fname):
    return os.path.abspath(os.path.dirname(fname))

here = absdir(__file__)

def first_gt(l, val):
    '''Return the index of the first element of l greater than val.

    If none exists, return None.
    '''
    try:
        return [t > val for t in l].index(True)
    except ValueError:
        return None

def vbound(*rects):
    '''Get the vertical bounds of a collection of rectangles'''
    m = float("inf")
    M = float("-inf")
    for (x, y, w, h) in rects:
        m = min(y, m)
        M = max(y + h, M)
    return m, M

def vcrop(im, y, Y):
    '''Vertically crop im from y to Y'''
    width, height = im.size
    if y < 0: y = 0;
    if Y >= height: Y = height-1
    if y < 0 or Y >= height:
        msg = "Bounds error: [{0},{1}] not in [0,{2}]"
        raise ValueError(msg.format(y, Y, height))
    return im.crop((0, y, width, Y))

def stack_ims(*ims):
    widths, heights = zip(*[i.size for i in ims])
    mw = max(widths)
    total_height = sum(heights)
    result = Image.new("RGB", (mw, total_height))
    y = 0
    for im in ims:
        result.paste(im, (0, y))
        y += im.size[1]
    return result

def crop_vid(src, dst, start, duration, codec=None, fadeout=0):
    '''Crop the video src from start for duration, saving to dst.

    Times should be in seconds or as strings that FFMPEG recognizes, e.g.
    1:05:11
    '''
    cmd = "ffmpeg -y -i {src} -ss {start} -t {duration} {dst}"
    if fadeout:
        raise Exception("Fadeout not working yet.")
        fadestart = duration
        duration = duration + fadeout
        cmd = cmd.replace("-t", "-af afade=t=out:st={fadestart}:d={fadeout} -t")
    if codec:
        cmd = cmd.replace("-t", "-codec {codec} -t")
    print cmd.format(**locals())
    import sys; sys.exit(1)
    os.system(cmd.format(**locals()))

class Span(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlaps(self, start, end):
        return start < self.end and end > self.start

    def offset_t(self, start):
        self.start -= start
        self.end -= start

class Measure(Span):
    def __init__(self, start, end, bounds):
        Span.__init__(self, start, end)
        self.bounds = bounds

    def offset_y(self, offset):
        self.bounds[1] -= offset

class Page(Span):
    """One page of a score"""
    def __init__(self, image, measures):
        self.image = image
        self.measures = measures
        self.n_measures = len(measures)
        start = measures[0].start
        end = measures[-1].end
        Span.__init__(self, start, end)

    @classmethod
    def from_json(cls, data, img, start_time):
        image = Image.open(img)
        ends = map(float, data['measure_ends'])
        starts = [start_time] + list(ends[:-1])
        bounds = [map(int, box) for box in data["measure_bounds"]]
        measures = [Measure(s,e,b) for s, e, b in zip(starts, ends, bounds)]
        return Page(image, measures)

class Score(object):
    def __init__(self, mp3, pages, data):
        self.mp3 = mp3
        self.ogg = self.mp3.replace("mp3", "ogg")
        self.pages = pages
        self.data = data

    def get_measure(self, mnum):
        measures_so_far = 0
        for page in self.pages:
            if mnum < measures_so_far + page.n_measures:
                break
            measures_so_far += page.n_measures
        else:
            raise Exception("No measure number {0}".format(mnum))
        return page.measures[mnum-measures_so_far]

def load(dirname):
    root = os.path.abspath(dirname)
    data = json.load(open(root+"/data.js"))
    pages = []
    start_time = 0
    for i, pdict in enumerate(data['pages']):
        img = root+"/pages/{0}.jpg".format(i+1)
        pages.append(Page.from_json(pdict, img, start_time))
        start_time = pages[-1].end
    mp3 = root+"/music.mp3"
    return Score(mp3, pages, data)

def draw(page):
    im = page.image.copy()
    draw = ImageDraw.Draw(im)
    for measure in page.measures:
        (lx, ly, w, h) = measure.bounds
        bounds = (lx, ly, (lx+w), (ly+h))
        draw.rectangle(bounds, None, 0)
    im.show()

@app.subcommand()
def crop1(input_dir, output_dir, start, end):
    # Get input folder, output folder, bounds
    start = float(start)
    end = float(end)
    dur = end-start
    # Make the output folder
    os.system('mkdir -p ' + output_dir)
    os.system('mkdir -p ' + output_dir+"/pages")
    # Load the input data
    score = load(input_dir)
    # Crop the MP3
    crop_vid(score.mp3, output_dir+"/music.mp3", start, dur)
    crop_vid(score.ogg, output_dir+"/music.ogg", start, dur, codec="libvorbis")
    blocks = []
    for page in score.pages:
        if not page.overlaps(start, end): continue
        im = page.image
        measures = [m for m in page.measures if m.overlaps(start,end)]
        measures = [copy.copy(m) for m in measures]
        vbounds = vbound(*[m.bounds for m in measures])
        im = vcrop(im, *vbounds)
        for m in measures:
            m.offset_t(start)
            m.offset_y(vbounds[0])
        blocks.append(Page(im, measures))
    # Concatenate all images to get final image
    new_im = stack_ims(*[p.image for p in blocks])
    # Concatenate measures, adjusting for images
    new_measures = []
    h = 0
    for p in blocks:
        measures = [copy.copy(m) for m in p.measures]
        for m in measures:
            m.offset_y(-h)
        new_measures.extend(measures)
        h += p.image.size[1]
    new_page = Page(new_im, new_measures)
    # draw(new_page)
    new_page.image.save(output_dir+"/pages/1.jpg")
    # Convert to mtimes, mbounds for output
    d = {}
    d['measure_ends'] = [m.end for m in new_page.measures]
    d['measure_bounds'] = [m.bounds for m in new_page.measures]
    d = dict(title=score.data['title'], pages=[d])
    json.dump(d, open(output_dir+"/data.js", 'w'))

@app.subcommand()
def crop_measures(input_dir, output_dir, mstart, mend):
    score = load(input_dir)
    start = score.get_measure(int(mstart)-1).start
    end = score.get_measure(int(mend)-1).end
    crop1(input_dir, output_dir, start, end)

@app.subcommand()
def info(input_dir, mnum):
    score = load(input_dir)
    m = score.get_measure(int(mnum)-1)
    print "Measure {0} goes from {1} to {2}".format(mnum, m.start, m.end)

@app.subcommand()
def all_crops(input_dir):
    data = json.load(open(input_dir+"/segments.js"))
    in_parent = os.path.dirname(os.path.normpath(input_dir))
    in_name = os.path.basename(os.path.normpath(input_dir))
    for name, (start, end) in data.items():
        output_dir = os.path.join(in_parent, in_name + name)
        crop1(input_dir, output_dir, start, end)

@app.subcommand()
def tmp():
    def t(i): return "tracks/0%i\\ Track\\ 0%i.mp3"%(i,i)
    crop_vid(t(2), "senta/music.mp3", 18, 30-18)
    crop_vid(t(3), "dutchmanparody/music.mp3", 256, 8)
    crop_vid(t(5), "dutchmanself/music.mp3", 192, 16)
    crop_vid(t(8), "dstimpani/music.mp3", 9, 4)
    crop_vid(t(8), "dsstrings/music.mp3", 37, 7)


if __name__ == '__main__':
    app.run()
