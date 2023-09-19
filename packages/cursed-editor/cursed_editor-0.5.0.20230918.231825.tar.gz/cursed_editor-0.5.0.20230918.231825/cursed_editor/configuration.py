#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2023 Philip Zerull

# This file is part of "The Cursed Editor"

# "The Cursed Editor" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

import os
import io
import configparser

from pathlib import Path


class Config:
    def __init__(self):
        self._parser = configparser.ConfigParser(default_section="default")
        default_configuration = {
            "default": {"tab_display_width": 4, "expand_tabs": 0},
            "extension:py": {"expand_tabs": 4},
        }
        self._parser.read_dict(default_configuration)
        self._path_of_file_to_edit = None

    def read_project_configuration(self, path_of_file_to_edit):
        self._path_of_file_to_edit = path_of_file_to_edit
        paths = self._get_project_configuration(path_of_file_to_edit)
        self.read(paths)

    def read(self, filepath, encoding=None):
        self._parser.read(filepath, encoding=encoding)

    def _get_project_configuration(self, path_of_file_to_edit=None):
        result = []
        if path_of_file_to_edit is None:
            parents = Path(os.getcwd())
            parents = [parents] + list(parents.parents)
        else:
            parents = list(Path(path_of_file_to_edit).parents)
        for folder in parents:
            testpath = folder.joinpath(".cursed.conf")
            if os.path.exists(testpath):
                result.append(testpath)
                break
        return result

    def write_config_to_string(self):
        fref = io.StringIO()
        self._parser.write(fref)
        fref.seek(0)
        return fref.read()

    def _get_section(self):
        if self._path_of_file_to_edit is None:
            return self._parser["default"]
        path = Path(self._path_of_file_to_edit)
        section = "extension:" + "".join(path.suffixes)[1:]
        if self._parser.has_section(section):
            return self._parser[section]
        section = "extension:" + path.suffix[1:]
        if self._parser.has_section(section):
            return self._parser[section]
        return self._parser["default"]

    @property
    def tab_display_width(self):
        section = self._get_section()
        return section.getint("tab_display_width")

    @property
    def expand_tabs(self):
        section = self._get_section()
        return section.getint("expand_tabs")
