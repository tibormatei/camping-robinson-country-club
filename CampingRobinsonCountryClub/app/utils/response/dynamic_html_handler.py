# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dynamic_html_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handlers a static file.
"""

from utils.response import RequestHandler


class DynamicHtmlHandler(RequestHandler):
    """
    This class handlers a static file.
    """

    def __init__(self, page_builder):
        """
        The init method initialize instance attributes.

        Args:
            self: DynamicHtmlHandler self parameter.
            page_builder: Dynami page builder.
        """
        super().__init__()
        self._content_type = 'text/html'
        self._contents = bytes(page_builder.__str__(), "utf-8")
