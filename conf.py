#!/usr/bin/env python3
# Version 2.0, May 2020
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from misc.cyverse_sphinx_conf import *  # noqa

project = 'ag2pi_workshop'
copyright = '2021, CyVerse'
author = 'R Bartelme <bartelme@cyverse.org>'
version = '2.0'
release = '2.0'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
