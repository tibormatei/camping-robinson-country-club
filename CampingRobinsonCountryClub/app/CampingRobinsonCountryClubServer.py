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
from Index import Index


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
        self._connectionIsKeepAlive = True

    def do_GET(self):
        """
        @summary: By design the http protocol has a “get” request.
        """
        if self.path == '/':
            self._sendIndexPage()
        else:
            (mime_type, encoding) = mimetypes.guess_type(self.path)
            if mime_type is not None:
                print(mime_type)
                match mime_type:
                    case 'text/html':
                        self._sendIndexPage()

                    case 'image/x-icon' | 'image/vnd.microsoft.icon':
                        self._sendIcoImage(self.path)

                    case 'image/png':
                        self._sendPngImage(self.path)

                    case _:
                        pass

    def do_POST(self):
        """
        @summary: By design the http protocol has a “post” request.
        """
        pass

    def _sendIndexPage(self):
        """
        @summary: Send out index.html page.
        """
        index: Index = Index(self._rootPath)
        content = bytes(index.buildIndexPage(), "utf-8")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()

        self.wfile.write(content)

    def _sendIcoImage(self, path: str):
        if path.startswith("/"):
            path = path[1:]
        iconPath: Path = self._rootPath.joinpath(path)

        try:
            with open(iconPath, 'rb') as f:
                    icoData = f.read()
        except FileNotFoundError:
            # To do: It will create dynamically in default icon and return ok instance of error!
            print('404 - Favicon not found!')
            self.send_error(404, "Favicon not found!")

        self.send_response(200)
        self.send_header('Content-type', 'image/vnd.microsoft.icon')
        self.send_header('Content-Length', str(len(icoData)))
        self.end_headers()

        try:
            self.wfile.write(icoData)
            self.wfile.flush()
        except ConnectionAbortedError:
            print('Client disconnected early!')
            self.close_connection

    def _sendPngImage(self, path: str):
        if path.startswith("/"):
            path = path[1:]
        pngPath: Path = self._rootPath.joinpath(path)

        try:
            with open(pngPath, 'rb') as f:
                    pngData = f.read()
        except FileNotFoundError:
            print('404 - Png image not found!')
            self.send_error(404, "Png image not found!")

        try:
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.send_header('Content-Length', str(len(pngData)))
            self.end_headers()
            self.end_headers()

            self.wfile.write(pngData)
            self.wfile.flush()
        except ConnectionAbortedError:
            print('Client disconnected early!')
