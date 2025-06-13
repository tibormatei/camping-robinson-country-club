# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: CampingRobinsonCountryClubServer.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is the web server.
"""

from http.server import BaseHTTPRequestHandler
from pathlib import Path
import mimetypes
import threading

from Index import Index
from utils.response import *


class CampingRobinsonCountryClubServer(BaseHTTPRequestHandler):
    """
    @summary: This class controll the web server.
    """

    protocol_version = "HTTP/1.1"

    def setup(self):
        """
        @summary: My own setups.
        @param self: CampingRobinsonCountryClubServer self parameter.
        """
        # REQUIRED to call base setup:
        super().setup()

        # Custom initializations:
        self._rootPath: Path = Path(__file__).parent

    def do_GET(self):
        """
        @summary: By design the http protocol has a “get” request.
                  This is an asynchronous thread handler.
        """
        print(f"Request handled in thread: {threading.current_thread().ident}")

        if self.path == '/':
            # sendIndexPage:
            indexPageCreator: Index = Index(self._rootPath)
            handler = DynamicHtmlHandler(indexPageCreator)
        else:
            (mimeType, encoding) = mimetypes.guess_type(self.path)
            if mimeType is not None:
                match mimeType:
                    case 'text/html':
                        # sendIndexPage:
                        if self.path.find('index'):
                            indexPageCreator: Index = Index(self._rootPath)
                            handler = DynamicHtmlHandler(indexPageCreator)

                    case 'image/x-icon' | 'image/vnd.microsoft.icon':
                        # sendIcoImage:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'image/png':
                        # sendPngImage:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case _:
                        handler = BadRequestHandler()
        self.respond(handler)

    def do_POST(self):
        """
        @summary: By design the http protocol has a “post” request.
        """
        pass

    def respond(self, handler: RequestHandler):
        """
        @summary: Send a http respons.
        @param handler: Respons specific handler.
        """
        try:
            if not self.close_connection:
                # Set header:
                if handler.StatusCode == 200:
                    self.send_response(handler.StatusCode)
                    self.send_header("Content-type", handler.ContentType)
                    self.send_header('Content-Length', handler.ContentLength)
                    self.end_headers()

                    # Set contents:
                    if not self.wfile.closed:
                        self.wfile.write(handler.Contents)
                        self.wfile.flush()
                else:
                    self.send_error(handler.StatusCode, str(handler.Contents, 'utf-8'))

        except ConnectionAbortedError:
                print('Client disconnected early!')
