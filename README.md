# Texture Packer CLI tool

Texture Packer (based on http://www.executionunit.com/blog/2013/04/12/python-script-to-build-a-texture-page-or-sprite-sheet/ by Execution Unit Ltd.)

![3-clause BSD license](https://img.shields.io/github/license/brean/python-txtrpacker)
![PyPI](https://img.shields.io/pypi/v/txtrpacker)

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

## Algorithm

The algorithm we are going to use in called Bin Packing. We want to pack the textures in to one larger texture with the minimum of wasted space. Note that there will always be some wasted space, this is an NP complete problem and Bin Packing just gives you a very good solution not a perfect one

2D bin packing works by using the source images to subdivide the destination image creating a tree of 'used' areas of the destination image. This sounds a little complication but it's actually pretty simple.


## Usage

The python code can be run from the command line to pack a set of PNGs that are in a directory:

```bash

    usage: txtrpacker [-h] [-v] [-pad PAD] [-sort SORT] [-maxdim MAXDIM]
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

```bash
$ txtrpacker -pad 4 ./testart output.png
```

## Contributing

Please use the [issue tracker](https://github.com/brean/python-txtrpacker/issues) to submit bug reports and feature requests.

## License

python-txtrpacker is distributed under the [3-clause BSD license](https://opensource.org/license/bsd-3-clause/).

## Maintainer

Andreas Bresser, self@andreasbresser.de

## Authors / Contributers
Authors and contributers are [listed on github](https://github.com/brean/python-txtrpacker/graphs/contributors).
