#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2020 Scriptim (https://github.com/Scriptim)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re

import numpy
import setuptools
from Cython.Build import cythonize
from setuptools.extension import Extension

extensions = [
    Extension(
        "game_static",
        ["abalone_engine/game_static.pyx", ],
        include_dirs=[numpy.get_include()],
    ),
]
with open('README.md', 'r') as readme:
    long_description = readme.read()
    github_url_prefix = '(https://github.com/Scriptim/Abalone-BoAI/tree/master/'
    github_raw_url_prefix = '(https://raw.githubusercontent.com/Scriptim/Abalone-BoAI/master/'
    long_description = re.sub(
        '\\(\\./img/', github_raw_url_prefix + 'img/', long_description)
    long_description = re.sub('\\(\\./', github_url_prefix, long_description)

setuptools.setup(
    name='abalone-engine',
    version='1.3.2',
    author='Scriptim',
    author_email='Scriptim@gmx.de',
    description='A Python implementation of the board game intended to be played by artificial intelligence',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Scriptim/Abalone-BoAI',
    packages=['abalone_engine',
              'abalone_engine/players'],
    package_data={
        "abalone_engine": ["lib/*.jar"],
    },
    ext_modules=cythonize(extensions),
    install_requires=['colorama', 'inquirer'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    python_requires='>=3.6',
)
