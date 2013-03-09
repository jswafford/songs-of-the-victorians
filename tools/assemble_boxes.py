#!/usr/bin/env python
'''
Assumes times.js and svg/*.svg

Creates boxes.js
'''
import sys
import os
import glob
import json
import pprint

from consolation.app import Console

from extract_boxes import get_boxes

app = Console("")

def assemble_json(dirname):
    block = []
    f = lambda *x: os.path.join(dirname, *x)
    times = ['{0:.1f}'.format(i) for i in json.load(open(f("times.js")))]
    tindex = 0
    for page in glob.glob(f("svg/*.svg")):
        i = int(page[-5])
        measure_bounds = get_boxes(page)
        measure_times = times[tindex:tindex+len(measure_bounds)]
        tindex += len(measure_bounds)
        block.append({'measure_times':measure_times,
                      'measure_bounds':measure_bounds})
    return pprint.pformat(block).replace("'", '"')

@app.main()
def main(dir):
    open(dir+'/boxes.js','w').write(assemble_json(dir))

if __name__ == '__main__':
    app.run()