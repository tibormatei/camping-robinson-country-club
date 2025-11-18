# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: index.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class creates index.html.
"""

from pathlib import Path

from utils.generators import RentalDetailsSection
from utils.generators import LanguageOptionsForSelect


class Index():
    """
    This class creates index.html.
    """

    # Class variables
    INDEX_FILE_NAME: str = 'index.html'

    def __init__(self, path: str, translations: dict):
        """
        The init method initialize instance attributes.

        Args:
            self: Index self parameter.
            path: Root path.
        """
        self._index_file_path: Path = Path(path).joinpath('templates', self.__class__.INDEX_FILE_NAME)
        self._index_file_content: str = self.__read_index_html()
        self._translations: dict = translations

    def build_index_page(self) -> str:
        """
        Return the done index page.

        Args:
            self: Index self parameter.
        """
        # Replace langCode:
        LANG_CODE_KEY: str = 'langCode'
        self.__replace_in_index_content(LANG_CODE_KEY, self._translations[LANG_CODE_KEY])

        # Replace languageOptions:
        language_options_for_select: LanguageOptionsForSelect = LanguageOptionsForSelect(self._translations[LANG_CODE_KEY])
        language_options_for_select_html = language_options_for_select.generate_language_options_for_select()

        LANGUAGE_OPTIONS_KEY: str = 'languageOptions'
        self.__replace_in_index_content(LANGUAGE_OPTIONS_KEY, language_options_for_select_html)

        # Replace menu:
        MENU_KEY: str = 'menu'
        self.__replace_in_index_content(MENU_KEY, self._translations[MENU_KEY])

        # Replace rentaldetails:
        rental_details_section: RentalDetailsSection = RentalDetailsSection()
        rental_details_section_html = rental_details_section.generate_rental_details_section(self._translations)

        RENTALDETAILS_KEY: str = 'rentaldetails'
        self.__replace_in_index_content(RENTALDETAILS_KEY, rental_details_section_html)

        return self._index_file_content
    
    def __replace_in_index_content(self, key: str, content: str) -> str:
        """
        Replace the given key to the given content.

        Args:
            cls: Index cls parameter.
        """
        self._index_file_content = self._index_file_content.replace('{{' + key + '}}', content)

    def __read_index_html(self) -> str:
        """
        Read in index.html from templates folder.

        Args:
            self: Index self parameter.
        Returns:
            Returns contents of html file.
        """
        index_html: str = None

        try:
            with open(self._index_file_path, 'r', encoding = 'utf-8') as f:
                index_html = f.read()
        except FileNotFoundError:
            print(f"Exception Error: {self._index_file_path} file not found!")
            index_html = "Server error!"
        except Exception as e:
            print(f"Exception Error: reading {self._index_file_path}: {e}")
            index_html = "Server html file error!"

        return index_html

    def __str__(self) -> str:
        """
        A function of a class that can return index.html page.
        """
        return self.build_index_page()
