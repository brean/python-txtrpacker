"""Command line interface for txtrpacker."""
import os
from glob import glob

import argparse
import logging
from PIL import Image
from .txtrpacker import sort_heuristics, pack_images

log = logging.getLogger(__name__)


def main():
    _description = """A utility to take a set of png images and pack them in to
    a power of two image with padding. The placements of the source images is
    printed to stdout in the format: "filename x y x2 y2"
    """

    _epilog = " example: txtrpacker images/ output.png"

    parser = argparse.ArgumentParser(description=_description, epilog=_epilog)
    parser.add_argument(
        "-v", action="store_true",
        help="enable verbose mode",
        default=False)
    parser.add_argument(
        "-pad", type=int,
        help="padding on each side of the texture (default: 2)",
        default=2)
    heuristic_keys = ",".join(sort_heuristics.keys())
    parser.add_argument(
        "-sort", type=str, default="maxarea",
        help=f"sort algorithm one of {heuristic_keys} (default: maxarea)")
    parser.add_argument("-maxdim", type=int, default=4096,
                        help="maximum texture size permissable.")
    parser.add_argument(
        "--log", type=str,
        help="Logging level (INFO, DEBUG, WARN) (default: INFO)",
        default="INFO")
    parser.add_argument("src", type=str, help="src directory")
    parser.add_argument("dst", type=str, help="dest png file")

    args = parser.parse_args()
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        log.error('Invalid log level: %s', args.log)
        return
    logging.basicConfig(level=numeric_level)

    if args.sort not in sort_heuristics:
        log.error("Unknown sort parameter '%s'", args.sort)
        return

    #get a list of PNG files in the current directory
    names = glob(os.path.join(args.src, "*.png"))
    #create a list of PIL Image objects, sorted by size
    images = [(name, Image.open(name)) for name in names]

    placements = pack_images(images, args.pad, args.sort, args.maxdim, args.dst)
    for area, name, _ in placements:
        print(f'{name} {area.x1} {area.y1} {area.x2} {area.y2}')


if __name__ == "__main__":
    main()
