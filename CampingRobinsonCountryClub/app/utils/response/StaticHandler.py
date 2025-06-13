# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: StaticHandler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handlers a static file.
"""

from pathlib import Path

from .RequestHandler import RequestHandler


class StaticHandler(RequestHandler):
    """
    @summary: This class handlers a static file.
    """

    def __init__(self, rootPath: Path, path: str = '/', mimeType: str = '', cache = None):
        """
        @summary: The init method initialize instance attributes.
        @param self: StaticHandler self parameter.
        @param mimeType: File mime type.
        @param path: File path.
        @param cache: Cached files.
        """
        super().__init__()
        self._contentType = mimeType

        if cache is None:
            # Reading from the file system.
            if path.startswith("/"):
                path = path[1:]
            staticFilePath: Path = rootPath.joinpath(path)

            try:
                with open(staticFilePath, 'rb') as f:
                    self._contents = f.read()

            except FileNotFoundError:
                self._statusCode = 404
                self._contents = bytes(f"{path} file Not found!", 'utf-8')
        else:
            # To Do: future support!
            pass
