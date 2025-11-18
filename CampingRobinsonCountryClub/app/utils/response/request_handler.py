# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: request_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is base Handler class.
"""


class RequestHandler():
    """
    This class is base Handler class.
    """

    def __init__(self):
        """
        The init method initialize instance attributes.

        Args:
            self: RequestHandler self parameter.
        """
        self._status_code: int = 200
        self._content_type: str = str()
        self._contents: bytes = bytes()

    @property
    def status_code(self) -> int:
        """
        The status_code getter property.

        Args:
            self: RequestHandler self parameter.
        Returns:
            Request status code, default is 200.
        """
        return self._status_code
    
    @property
    def content_type(self) -> str:
        """
        The content_type getter property.

        Args:
            self: RequestHandler self parameter.
        Returns:
            Mime type of contents.
        """
        return self._content_type

    @property
    def contents(self) -> bytes:
        """
        The contents getter property.

        Args:
            self: RequestHandler self parameter.
        Returns:
            A File contents.
        """
        return self._contents

    @property
    def content_length(self) -> str:
        """
        The content_length getter property.

        Args:
            self: RequestHandler self parameter.
        Returns:
            Contents's length in str.
        """
        return str(len(self._contents))
