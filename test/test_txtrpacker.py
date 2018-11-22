#!/usr/bin/env python
# -*- coding: utf-8 -*-
from txtrpacker.txtrpacker import pack_images
import os
import glob
from PIL import Image


def test_pack_images():
    #get a list of PNG files in the current directory
    names = glob.glob(os.path.join('images', "*.png"))
    #create a list of PIL Image objects, sorted by size
    images = [(name, Image.open(name)) for name in names]

    placements = pack_images(images, padding=2, sort='maxarea', maxdim=2048, dstfilename='out.png')
    for area, name, im in placements:
        print("%s %d %d %d %d" % (name, area.x1, area.y1, area.x2, area.y2))


if __name__ == '__main__':
    test_pack_images()
