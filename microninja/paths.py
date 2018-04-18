#!/usr/bin/env python

# paths.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja

'''
Discovers and exposes the absolute pathnames for common_css_dir and common_images_dir
'''

import os

# setting up directories
dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../microninja-toolset'))

# media dir
media_local = os.path.join(dir_path, 'media')
media_usr = '/usr/share/microninja/media'

if os.path.exists(media_local):
    common_media_dir = media_local
elif os.path.exists(media_usr):
    common_media_dir = media_usr
else:
    raise Exception('Neither local nor usr media dir found!')

common_css_dir = os.path.join(common_media_dir, 'CSS')
common_images_dir = os.path.join(common_media_dir, 'images')
