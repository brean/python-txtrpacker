#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="txtrpacker",
    description="Texture Packer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/python-txtrpacker",
    version="0.3",
    license="BSD",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=['Pillow'],
    entry_points={
        'console_scripts': [
            'txtrpacker = txtrpacker.cli:main',
        ],
    }
)
