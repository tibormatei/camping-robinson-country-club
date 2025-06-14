# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: request_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is base Handler class.
"""


class RequestHandler():
    """
    @summary: This class is base Handler class.
    """

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: RequestHandler self parameter.
        """
        self._statusCode: int = 200
        self._contentType: str = str()
        self._contents: bytes = bytes()

    @property
    def StatusCode(self) -> int:
        """
        @summary: The StatusCode getter property.
        @param self: RequestHandler self parameter.
        @returns: Request status code, default is 200.
        """
        return self._statusCode
    
    @property
    def ContentType(self) -> str:
        """
        @summary: The ContentType getter property.
        @param self: RequestHandler self parameter.
        @returns: Mime type of contents.
        """
        return self._contentType

    @property
    def Contents(self) -> bytes:
        """
        @summary: The Contents getter property.
        @param self: RequestHandler self parameter.
        @returns: A File contents.
        """
        return self._contents

    @property
    def ContentLength(self) -> str:
        """
        @summary: The ContentLength getter property.
        @param self: RequestHandler self parameter.
        @returns: Contents's length in str.
        """
        return str(len(self._contents))
