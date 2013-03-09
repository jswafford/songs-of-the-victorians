#!/usr/bin/env python
'''
Insert images into the frame template.

Assuming /path/to/foobar/pages contains 1.jpg, 2.jpg, etc., call:
python apply_template create_svgs /path/to/foobar

This creates /path/to/foobar/svg/ containing 1.svg, 2.svg, etc.
'''
import sys
import os
import glob
import xml.etree.ElementTree as ET

from consolation.app import Console

app = Console("")

here = os.path.abspath(os.path.dirname(__file__))

@app.subcommand()
def insert_image(src, dst, img_pth):
    prefix = '{http://www.w3.org/2000/svg}'
    tree = ET.parse(src)
    image = tree.findall(prefix+"g/"+prefix+"image")
    assert len(image) == 1
    image = image[0]
    image.attrib['{http://www.w3.org/1999/xlink}href'] = img_pth
    tree.write(open(dst, 'w'))

@app.subcommand()
def create_svgs(target):
    src = os.path.join(here,"template.svg")
    os.system('mkdir {0}/svg'.format(target))
    for img_pth in glob.glob(os.path.join(target, "pages/*.jpg")):
        i = int(img_pth[-5])
        dst = os.path.join(target, "svg/{0}.svg".format(i))
        img_pth = '../pages/{0}.jpg'.format(i)
        insert_image(src, dst, img_pth)

@app.subcommand()
def rescale_tmp(src):
    scale = 740.0/750.0
    prefix = '{http://www.w3.org/2000/svg}'
    tree = ET.parse(src)
    image = tree.findall(prefix+"g/"+prefix+"image")
    assert len(image) == 1
    image = image[0]
    # del image.attrib['height'], image.attrib['width']
    rects = tree.findall(prefix+"g/"+prefix+"rect")
    for rect in rects:
        rect.attrib['height'] = `float(rect.attrib['height'])*scale`
        rect.attrib['y'] = `float(rect.attrib['y'])*scale`
        rect.attrib['width'] = `float(rect.attrib['width'])*scale`
        rect.attrib['x'] = `float(rect.attrib['x'])*scale`
    tree.write(open(src, 'w'))

if __name__ == '__main__':
    app.run()