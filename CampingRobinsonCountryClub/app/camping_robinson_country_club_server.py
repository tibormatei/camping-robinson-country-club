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
from utils.language import LanguageCodes


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

                    case 'image/jpeg':
                        # send JPGImage:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'text/css':
                        # send CssStyle:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'text/javascript' | 'application/javascript':
                        # send JavaScript:
                        handler = StaticHandler(self._rootPath, self.path, mimeType)

                    case 'text/json' | 'application/json':
                        # send json file:
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
        """
        cookies: dict[str, str] = self._parseCookie(self.headers.get('Cookie'))

        LANGUAGE_COOKIE: str = "language"
        if LANGUAGE_COOKIE in cookies:
            userLanguage = LanguageCodes[cookies[LANGUAGE_COOKIE]]
        else:
            userLanguage = self._parseAcceptLanguage(self.headers.get('Accept-Language', ''))

        language = self._getLanguageJson(userLanguage)

        indexPageCreator: Index = Index(self._rootPath, language)
        dynamicHtmlHandler = DynamicHtmlHandler(indexPageCreator)

        return dynamicHtmlHandler

    def _getLanguageJson(self, userLanguage: LanguageCodes):
        """
        @summary: Return language parsed json.
        @param self: CampingRobinsonCountryClubServer self parameter.
        @param userLanguage: Selected language enum.
        @return: Parsed language json dictionary.
        """
        languageFileName: str = userLanguage.name + '.json'
        languagePath = self._rootPath.joinpath('data', 'languages', languageFileName)
        try:
            f = open(file = languagePath, mode = 'r', encoding = 'utf-8')
            language = json.load(f)
            f.close()

        except FileNotFoundError:
            print(f'Language file not found: {languageFileName}!')
            language = {}

        return language

    def _parseAcceptLanguage(self, acceptLanguage: str) -> LanguageCodes:
        """
        @summary: Parse Accept-Language header and return prefered language of user.
        @param self: CampingRobinsonCountryClubServer self parameter.
        @param acceptLanguage: Accept-Language header string.
        @return: LanguageCodes enum value.
        """
        languageCode = LanguageCodes.en

        for languageStr in acceptLanguage.lower().split(','):
            if languageStr.startswith(LanguageCodes.en.name):
                languageCode = LanguageCodes.en
                break
            elif languageStr.startswith(LanguageCodes.hu.name):
                languageCode = LanguageCodes.hu
                break
            elif languageStr.startswith(LanguageCodes.ro.name):
                languageCode = LanguageCodes.ro
                break
            else:
                pass

        return languageCode

    def _parseCookie(self, cookie: str) -> dict:
        """
        @summary: Parse Cookie header and return a map with cookies.
        @param self: CampingRobinsonCountryClubServer self parameter.
        @param cookie: Cookie header string.
        @return: cookies in a dictionary.
        """
        cookies = dict()
        if cookie != None:
            cookieStrings = cookie.split('; ')
            for cookieString in cookieStrings:
                keyValueCookie = cookieString.split('=')
                if len(keyValueCookie) > 1:
                    cookies[keyValueCookie[0]] = keyValueCookie[1]

        return cookies
