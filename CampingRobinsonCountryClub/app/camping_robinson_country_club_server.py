# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: camping_robinson_country_club_server.py
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
import json

from index import Index
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
        @param self: CampingRobinsonCountryClubServer self parameter.
        """
        print(f"Request handled in thread: {threading.current_thread().ident}")

        if self.path == '/':
            # send IndexPage:
            handler = self._getIndexPageHandler()
        else:
            (mimeType, encoding) = mimetypes.guess_type(self.path)
            if mimeType is not None:
                match mimeType:
                    case 'text/html':
                        # send IndexPage:
                        if self.path.find('index'):
                            handler = self._getIndexPageHandler()

                    case 'image/x-icon' | 'image/vnd.microsoft.icon':
                        # send IcoImage:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'image/png':
                        # send PngImage:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'text/css':
                        # send CssStyle:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'text/javascript' | 'application/javascript':
                        # send JavaScript:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case _:
                        handler = BadRequestHandler()
        self.respond(handler)
        del(handler)

    def do_POST(self):
        """
        @summary: By design the http protocol has a “post” request.
        @param self: CampingRobinsonCountryClubServer self parameter.
        """
        pass

    def respond(self, handler: RequestHandler):
        """
        @summary: Send a http respons.
        @param self: CampingRobinsonCountryClubServer self parameter.
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

    def _getIndexPageHandler(self) -> DynamicHtmlHandler:
        """
        @summary: Get index page.
        @param self: CampingRobinsonCountryClubServer self parameter.
        @param self: Respons specific handler.
        """
        # accept_language = self.headers.get('Accept-Language', '')
        # print(f"Browser languages: {accept_language}")
        # To Do: decide which language you need!

        languagePath = self._rootPath.joinpath('data', 'languages', 'en.json')
        f = open(languagePath)
        language = json.load(f)

        indexPageCreator: Index = Index(self._rootPath, language)
        return DynamicHtmlHandler(indexPageCreator)
