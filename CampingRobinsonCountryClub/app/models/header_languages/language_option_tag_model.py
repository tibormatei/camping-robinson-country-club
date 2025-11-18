# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model for the option tag in the header language select.
"""


class LanguageOptionTagModel():
    """
    This class is a model of language option tag.
    """

    def __init__(self, display_language_name: str = '', language_code_name: str = '', selected: bool = False):
        """
        The init method initialize instance attributes.

        Args:
            self: LanguageOptionTagModel self parameter.
            display_language_name: Display Language Name the inner text.
            language_code_name: value parameter.
            selected: Is selected option.
        """
        self._display_language_name: str = display_language_name
        self._language_code_name: str = language_code_name
        self._selected: bool = selected

    @property
    def display_language_name(self) -> str:
        """
        The display_language_name getter property.

        Args:
            self: LanguageOptionTagModel self parameter.
        Returns:
            Language name.
        """
        return self._display_language_name

    @property
    def language_code_name(self) -> str:
        """
        The language_code_name getter property.

        Args:
            self: LanguageOptionTagModel self parameter.
        Returns:
            Language code naem for value parameter.
        """
        return self._language_code_name

    @property
    def is_selected(self) -> bool:
        """
        The Selected getter property.

        Args:
            self: LanguageOptionTagModel self parameter.
        Returns:
            Return True if the option is selected.
        """
        return self._selected
