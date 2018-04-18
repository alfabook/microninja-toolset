#!/usr/bin/env python

# kano_scrolled_window.py
#
# Copyright (C) 2014 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# Create a scrolled window with custom scrollbars

# Copyright (C) 2016 Alfabook srl
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
# rebadged with microninja

from gi.repository import Gtk
from microninja.paths import common_css_dir
from microninja.gtk3.apply_styles import apply_styling_to_widget, apply_styling_to_screen, apply_colours_to_widget
import os


class ScrolledWindow(Gtk.ScrolledWindow):
    NORMAL_CSS_PATH = os.path.join(common_css_dir, 'scrollbar.css')
    WIDE_CSS_PATH = os.path.join(common_css_dir, 'scrollbar-wide.css')

    def __init__(self, hexpand=None, vexpand=None, wide_scrollbar=False):
        Gtk.ScrolledWindow.__init__(self, hexpand=hexpand, vexpand=vexpand)

    @staticmethod
    def apply_styling_to_screen(wide=False):
        if wide:
            apply_styling_to_screen(ScrolledWindow.WIDE_CSS_PATH)
        else:
            apply_styling_to_screen(ScrolledWindow.NORMAL_CSS_PATH)

    def apply_styling_to_widget(self, wide=False):
        for bar in [self.get_vscrollbar(), self.get_hscrollbar()]:
            apply_colours_to_widget(bar)
            if wide:
                apply_styling_to_widget(bar, self.WIDE_CSS_PATH)
            else:
                apply_styling_to_widget(bar, self.NORMAL_CSS_PATH)
