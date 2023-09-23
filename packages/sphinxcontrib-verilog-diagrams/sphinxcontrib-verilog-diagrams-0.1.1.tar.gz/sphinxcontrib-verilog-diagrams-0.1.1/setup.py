#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2021  The SymbiFlow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

import sys
from os import path

from setuptools import setup, find_packages

__dir__ = path.dirname(path.abspath(__file__))
readme_file = path.join(__dir__, 'README.rst')
try:
    with open(readme_file) as f:
        readme = f.read()
except FileNotFoundError as e:
    import traceback
    traceback.print_exc()
    readme = ''
    __version__ = 'error'

install_requires = [
    'sphinxcontrib-hdl-diagrams'
]

setup(
    name='sphinxcontrib-verilog-diagrams',
    version="0.1.1",
    description='Compatibility stub for renamed to sphinxcontrib-hdl-diagrams.',
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="The SymbiFlow Authors",
    author_email='symbiflow@lists.librecores.org',
    url='https://github.com/SymbiFlow/sphinxcontrib-hdl-diagrams',
    packages=find_packages(),
    license="Apache 2.0",
    keywords='',
    classifiers=[],
    install_requires=install_requires,
)
