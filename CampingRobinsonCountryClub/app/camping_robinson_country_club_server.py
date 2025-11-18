# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: camping_robinson_country_club_server.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is the web server.
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
    This class controll the web server.
    """

    protocol_version = "HTTP/1.1"

    def setup(self):
        """
        My own setups.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
        """
        # REQUIRED to call base setup:
        super().setup()

        # Custom initializations:
        self._root_path: Path = Path(__file__).parent

    def do_GET(self):
        """
        By design the http protocol has a “get” request.
        This is an asynchronous thread handler.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
        """
        print(f"Request handled in thread: {threading.current_thread().ident}")

        if self.path == '/':
            # send IndexPage:
            handler = self._get_index_page_handler()
        else:
            (mime_type, encoding) = mimetypes.guess_type(self.path)
            if mime_type is not None:
                match mime_type:
                    case 'text/html':
                        # send IndexPage:
                        if self.path.find('index'):
                            handler = self._get_index_page_handler()

                    case 'image/x-icon' | 'image/vnd.microsoft.icon':
                        # send IcoImage:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case 'image/png':
                        # send PngImage:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case 'image/jpeg':
                        # send JPGImage:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case 'text/css':
                        # send CssStyle:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case 'text/javascript' | 'application/javascript':
                        # send JavaScript:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case 'text/json' | 'application/json':
                        # send json file:
                        handler = StaticHandler(self._root_path, self.path, mime_type)

                    case _:
                        handler = BadRequestHandler()
        self.respond(handler)
        del(handler)

    def do_POST(self):
        """
        By design the http protocol has a “post” request.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
        """
        pass

    def respond(self, handler: RequestHandler):
        """
        Send a http respons.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
            handler: Respons specific handler.
        """
        try:
            if not self.close_connection:
                # Set header:
                if handler.status_code == 200:
                    self.send_response(handler.status_code)
                    self.send_header("Content-type", handler.content_type)
                    self.send_header('Content-Length', handler.content_type)
                    self.end_headers()

                    # Set contents:
                    if not self.wfile.closed:
                        self.wfile.write(handler.contents)
                        self.wfile.flush()
                else:
                    self.send_error(handler.status_code, str(handler.contents, 'utf-8'))
        except ConnectionAbortedError:
                print('Client disconnected early!')

    def _get_index_page_handler(self) -> DynamicHtmlHandler:
        """
        Get index page.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
        """
        cookies: dict[str, str] = self._parse_cookie(self.headers.get('Cookie'))

        LANGUAGE_COOKIE: str = "language"
        if LANGUAGE_COOKIE in cookies:
            user_language = LanguageCodes[cookies[LANGUAGE_COOKIE]]
        else:
            user_language = self._parse_accept_language(self.headers.get('Accept-Language', ''))

        language = self._get_language_json(user_language)

        index_page_creator: Index = Index(self._root_path, language)
        dynamic_html_handler = DynamicHtmlHandler(index_page_creator)

        return dynamic_html_handler

    def _get_language_json(self, user_language: LanguageCodes):
        """
        Return language parsed json.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
            user_language: Selected language enum.
        Returns:
            Parsed language json dictionary.
        """
        language_file_name: str = user_language.name + '.json'
        language_path = self._root_path.joinpath('data', 'languages', language_file_name)
        try:
            f = open(file = language_path, mode = 'r', encoding = 'utf-8')
            language = json.load(f)
            f.close()
        except FileNotFoundError:
            print(f'Language file not found: {language_file_name}!')
            language = {}

        return language

    def _parse_accept_language(self, accept_language: str) -> LanguageCodes:
        """
        Parse Accept-Language header and return prefered language of user.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
            accept_language: Accept-Language header string.
        Returns:
            LanguageCodes enum value.
        """
        language_code = LanguageCodes.en

        for language_str in accept_language.lower().split(','):
            if language_str.startswith(LanguageCodes.en.name):
                language_code = LanguageCodes.en
                break
            elif language_str.startswith(LanguageCodes.hu.name):
                language_code = LanguageCodes.hu
                break
            elif language_str.startswith(LanguageCodes.ro.name):
                language_code = LanguageCodes.ro
                break
            else:
                pass

        return language_code

    def _parse_cookie(self, cookie: str) -> dict:
        """
        Parse Cookie header and return a map with cookies.

        Args:
            self: CampingRobinsonCountryClubServer self parameter.
            cookie: Cookie header string.
        Returns:
            cookies in a dictionary.
        """
        cookies = dict()
        if cookie != None:
            cookie_strings = cookie.split('; ')
            for cookie_string in cookie_strings:
                key_value_cookie = cookie_string.split('=')
                if len(key_value_cookie) > 1:
                    cookies[key_value_cookie[0]] = key_value_cookie[1]

        return cookies
