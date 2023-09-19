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

import abc
import os
import logging


logger = logging.getLogger(__name__)


class BaseFileHandler(abc.ABC):
    def __init__(self):
        self.file_path = None
        self.encoding = "utf-8"

    def read(self):
        raise NotImplementedError

    def save(self, content: str):
        raise NotImplementedError


class FileHandler(BaseFileHandler):
    def __init__(self):
        super().__init__()

    def read(self):
        if not os.path.exists(self.file_path):
            return ""
        with open(self.file_path, encoding=self.encoding) as fref:
            return fref.read()

    def save(self, content: str):
        with open(self.file_path, "w", encoding=self.encoding) as fref:
            fref.write(content)


class MemoryFileHandler(BaseFileHandler):
    def __init__(self):
        super().__init__()
        self._content = ""

    def read(self):
        return self._content

    def save(self, content):
        self._content = content
