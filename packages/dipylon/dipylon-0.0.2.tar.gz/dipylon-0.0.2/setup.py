#!/usr/bin/env python

# Copyright (c) 2023, Jay Kubo
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# (*) Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
# (*) Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
# (*) Neither the name of the copyright holder nor the names of its
#     contributors may be used to endorse or promote products derived from
#     this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from os import chdir
from os.path import abspath, join, split

chdir(split(abspath(__file__))[0])

with open('README.md', 'r') as f:
    long_description = f.read()

meta = dict(
    name='dipylon',
    provides=['dipylon'],
    requires=['requests', 'beautifulsoup4', 'lxml', 'python-slugify', 'numpy', 'pandas', 'plotly'],
    packages=['dipylon'],
    scripts=[join('scripts', 'dipylon')],
    version='0.0.2',
    description='Gateway for financial markets information from various online resources',
    author='Jay Kubo',
    author_email='jaykubo@outlook.com',
    url='https://github.com/jkubo/dipylon',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ]
)

try:
    from setuptools import setup
    meta['install_requires'] = meta.pop('requires')
except ImportError:
    from distutils.core import setup

setup(**meta)