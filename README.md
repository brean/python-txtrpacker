# txtrpacker

Texture Packer (based on [this blog article](http://www.executionunit.com/blog/2013/04/12/python-script-to-build-a-texture-page-or-sprite-sheet/) by Execution Unit Ltd.)

[![Coverage Status](https://coveralls.io/repos/github/brean/python-txtrpacker/badge.svg?branch=master)](https://coveralls.io/github/brean/python-txtrpacker?branch=master)

## Installation

This library is provided by pypi, so you can just install the current stable version using pip:
```
pip install txtrpacker
```

## Why pack textures/images?
If you're making a game then it's more efficient to tell the hardware:

```
    use packed texture 1
    draw primitive 1,2,3,4,5,6
    use packed texture 2
    draw primitive 7,8,9,10
```

than to

```
    use texture 1
    draw primitive 1
    use texture 2
    draw primitive 2
    ...
```

The less you do, the more efficient rendering is.

If you're making a website then again it's quicker to ask the client browser to load one large image (often called a sprite sheet) than to ask it to load many more smaller textures.

So what this library does is, it takes a folder containing some images and combines them into one big image. We have some example images in `test/images` which will be automatically positioned in an output image using the command `python test_txtrpacker.py` in the test/-folder:

![generated output image](https://raw.githubusercontent.com/brean/python-txtrpacker/v0.0.2/docs/images/out.png)


# Algorithm 
The algorithm we are going to use in called Bin Packing. We want to pack the textures in to one larger texture with the minimum of wasted space. Note that there will always be some wasted space, this is an NP complete problem and Bin Packing just gives you a very good solution not a perfect one

2D bin packing works by using the source images to subdivide the destination image creating a tree of 'used' areas of the destination image. This sounds a little complication but it's actually pretty simple.


# Usage
The python code can be run from the command line to pack a set of PNGs that are in a directory:

```

    usage: txtrpacker.py [-h] [-v] [-pad PAD] [-sort SORT] [-maxdim MAXDIM]
                     [--log LOG]
                     src dst

    A utility to take a set of png images and pack them in to a power of two image
    with pading. The placements of the source images is printed to stdout in the
    format: "filename x y x2 y2"

    positional arguments:
      src             src directory
      dst             dest png file

    optional arguments:
      -h, --help      show this help message and exit
      -v              enable verbose mode
      -pad PAD        padding on each side of the texture (default: 2)
      -sort SORT      sort algorithm one of maxheight,maxwidth,maxarea (default:
                      maxarea)
      -maxdim MAXDIM  maximum texture size permissable.
      --log LOG       Logging level (INFO, DEBUG, WARN) (default: INFO)

```

using the example data you could enter:

```
python txtrpacker.py -pad 4 ./test/images output.png
```
