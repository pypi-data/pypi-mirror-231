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
import curses
import time
import argparse
import logging
import logging.config
from .editor import Editor
from .key_handler import KeyHandler
from .file_handlers import BaseFileHandler, FileHandler
from .configuration import Config

VERSION = "unknown"

logger = logging.getLogger(__name__)


def setup_logging():
    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {},
            "filters": {},
            "handlers": {
                "file_handler": {
                    "class": "logging.FileHandler",
                    "level": "DEBUG",
                    "filename": "logfile.log",
                    "mode": "w",
                },
            },
            "disable_existing_loggers": False,
            "loggers": {},
            "root": {
                "level": "DEBUG",
                "handlers": ["file_handler"],
            },
        }
    )
    logger.info("logging initiated")


class Application:
    def __init__(self, file_handler: BaseFileHandler, config: Config):
        self.stdscr = None
        self.file_handler = file_handler
        self.config = config
        self.editor = Editor(
            file_handler,
            tab_size=config.tab_display_width,
            expand_tabs=config.expand_tabs,
        )
        self.key_handler = KeyHandler(self.editor)

    def main(self):
        os.environ.setdefault("ESCDELAY", "25")
        curses.wrapper(self.wrapped_curses_app)

    def wrapped_curses_app(self, stdscr):
        try:
            self.initialize_screen(stdscr)
            curses.use_default_colors()
            self.mainloop()
        except KeyboardInterrupt:
            logger.info("got keyboard interrupt. Closing application")
        except Exception as err:  # pragma: no cover pylint: disable=broad-except
            logger.exception(err)

    def initialize_screen(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.keypad(True)
        self.stdscr.clear()
        self.stdscr.nodelay(1)
        self.set_size()
        self.redraw_from_editor()

    def set_size(self):
        self.height, self.width = self.stdscr.getmaxyx()

    @property
    def width(self):
        return self.editor.window.width

    @width.setter
    def width(self, value):
        self.editor.window.width = value

    @property
    def height(self):
        return self.editor.window.height

    @height.setter
    def height(self, value):
        self.editor.window.height = value

    def mainloop(self):
        logger.info("mainloop started")
        while True:
            self.check_resize()
            self.check_keypress()
            time.sleep(0.01)

    def check_resize(self):
        if curses.is_term_resized(self.height, self.width):
            self.handle_resize()
            self.redraw_from_editor()

    def handle_resize(self):
        logger.info("New Screen Size: %s", self.stdscr.getmaxyx())
        self.set_size()

    def check_keypress(self):
        key = self.get_key()
        if key is not None:
            self.handle_key(key)

    def get_key(self):
        key = None
        try:
            key = self.stdscr.getkey()
        except curses.error:
            pass
        return key

    def handle_key(self, key):
        logger.info('Typed Character: key="%s" ordinal=%s', key, ord(key[:1]))
        logger.info("length=%s", len(key))
        if key == "KEY_RESIZE":
            self.check_resize()
        else:
            self.key_handler.handle_key(key)
            self.redraw_from_editor()

    def redraw_from_editor(self):
        self.stdscr.clear()
        self.move_cursor(x=0, y=0)
        text = self.editor.get_text_for_window()
        for y, line in enumerate(text.split("\n")):
            for x, char in enumerate(line):
                self.draw_character(char, x, y)
        self.move_cursor(
            x=self.editor.window_cursor_x, y=self.editor.window_cursor_y
        )

    def draw_character(self, character, x, y):
        try:
            self.stdscr.addch(y, x, character[:1])
        except curses.error:
            pass

    def move_cursor(self, *, x, y):
        x = min(self.width - 1, max(0, x))
        y = min(self.height - 1, max(0, y))
        self.stdscr.move(y, x)


def main(*, args=None, stdout=None, file_handler=None):
    setup_logging()
    parser = argparse.ArgumentParser(
        prog="cursed",
        description="A Vim inspired Text Editor Written in Pure Python",
    )
    parser.add_argument(
        "-c",
        "--config_file",
        help="The path to the user's config file",
        default=os.path.expanduser("~/.cursed.conf"),
    )
    parser.add_argument(
        "--keymap", help="Show the Key Bindings", action="store_true"
    )
    parser.add_argument(
        "--print_config",
        help="Print the current configuration",
        action="store_true",
    )
    parser.add_argument(
        "--version", help="Print the Program Version", action="store_true"
    )
    parser.add_argument("filename", help="The file to edit", nargs="?")

    parsed = parser.parse_args(args)
    config = Config()
    config.read(parsed.config_file)
    config.read_project_configuration(parsed.filename)
    if file_handler is None:
        file_handler = FileHandler()
    if parsed.filename is not None:
        file_handler.file_path = parsed.filename
        app = Application(file_handler, config=config)
        app.main()
    elif parsed.version:
        print(VERSION, file=stdout)
    elif parsed.keymap:
        print(KeyHandler.help_text(), file=stdout)
    elif parsed.print_config:
        print(config.write_config_to_string(), file=stdout)
    else:
        print(parser.format_help(), file=stdout)


if __name__ == "__main__":
    main()
VERSION = "0.5.0.20230918.235438+e19bd6651bfa728e5c259ea0d24e8be6a9a923fa"
