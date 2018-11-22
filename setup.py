#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="txtrpacker",
    description="Texture packer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/txtrpacker",
    version="0.0.2",
    author="Andreas Bresser, Execution Unit Ltd.",
    author_email="self@andreasbresser.de",
    packages=find_packages(),
    tests_require=[],
    include_package_data=True,
    classifiers=['Development Status :: 4 - Beta'],
    install_requires=[]
)
