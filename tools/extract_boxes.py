#!/usr/bin/env python
import sys
import xml.etree.ElementTree as ET

def box_gt(box1, box2):
    if abs(box1[1] - box2[1]) < 10:
        return 1 if box1[0] > box2[0] else -1
    return 1 if box1[1] > box2[1] else -1


def get_boxes(filename):
    prefix = '{http://www.w3.org/2000/svg}'
    tree = ET.parse(filename)
    nodes = tree.findall(prefix+"g/"+prefix+"rect")
    image = tree.findall(prefix+"g/"+prefix+"image")
    assert len(image) == 1
    image = image[0]
    offx = float(image.attrib['x'])
    offy = float(image.attrib['y'])
    src = image.attrib['{http://www.w3.org/1999/xlink}href']
    l = []
    for node in nodes:
        tx = ty = 0
        flip_x = False
        xform = node.attrib.get('transform', "translate(0,0)")
        if xform.startswith('translate'):
            tx, ty = map(float, xform[10:-1].split(','))
        elif xform == 'scale(-1,1)':
            flip_x = True
        width = float(node.attrib['width'])
        height = float(node.attrib['height'])
        x = float(node.attrib['x'])
        y = float(node.attrib['y']) - offy + ty
        if flip_x:
            x = -x-width
        x = x - offx + tx
        l.append(map(int, [x, y, width, height]))
    l.sort(box_gt)
    return l
