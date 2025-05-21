# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dynamic_html_handler.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handlers a static file.
"""

from utils.response import RequestHandler


class DynamicHtmlHandler(RequestHandler):
    """
    @summary: This class handlers a static file.
    """

    def __init__(self, pageBuilder):
        """
        @summary: The init method initialize instance attributes.
        @param self: DynamicHtmlHandler self parameter.
        @param pageBuilder: Dynami page builder.
        """
        super().__init__()
        self._contentType = 'text/html'
        self._contents = bytes(pageBuilder.__str__(), "utf-8")
