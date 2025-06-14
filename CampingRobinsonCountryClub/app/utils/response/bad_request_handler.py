# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: bad_request_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handlers a bad request file.
"""

from utils.response import RequestHandler


class BadRequestHandler(RequestHandler):
    """
    @summary: This class handlers a bad request file.
    """

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: StaticHandler self parameter.
        """
        super().__init__()
        self._contentType = 'text/plain'
        self._contents = bytes("404 - Not Found", "utf-8")
        self._statusCode = 404
