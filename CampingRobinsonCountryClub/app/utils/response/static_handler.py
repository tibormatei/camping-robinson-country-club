# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: static_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handlers a static file.
"""

from pathlib import Path

from utils.response import RequestHandler


class StaticHandler(RequestHandler):
    """
    This class handlers a static file.
    """

    def __init__(self, root_path: Path, path: str = '/', mime_type: str = '', cache = None):
        """
        The init method initialize instance attributes.

        Args:
            self: StaticHandler self parameter.
            mimeType: File mime type.
            path: File path.
            cache: Cached files.
        """
        super().__init__()
        self._content_type = mime_type

        if cache is None:
            # Reading from the file system.
            if path.startswith("/"):
                path = path[1:]
            static_file_path: Path = root_path.joinpath(path)

            try:
                with open(static_file_path, 'rb') as f:
                    self._contents = f.read()

            except FileNotFoundError:
                self._status_code = 404
                self._contents = bytes(f"{path} file Not found!", 'utf-8')
        else:
            # To Do: future support!
            pass
