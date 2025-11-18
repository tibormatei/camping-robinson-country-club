# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the language option tag model and view.
"""

from models.header_languages import LanguageOptionTagModel
from views.header_languages import LanguageOptionTagView


class LanguageOptionTagController():
    """
    This class controller the language option tag details.
    """

    def __init__(self, language_option_tag_model: LanguageOptionTagModel, language_option_tag_view: LanguageOptionTagView):
        """
        The init method initialize instance attributes.

        Args:
            self: LanguageOptionTagController self parameter.
            language_option_tag_model: The model class for MVC pattern.
            language_option_tag_view: The view class for MVC pattern.
        """
        self._language_option_tag_model: LanguageOptionTagModel = language_option_tag_model
        self._language_option_tag_view: LanguageOptionTagView = language_option_tag_view

    def show_language_option_tag(self) -> str:
        """
        Return the view of tent.

        Args:
            self: LanguageOptionTagController self parameter.
        Returns:
            Returns view of Language Option Tag in string.
        """
        return self._language_option_tag_view.show_language_option_tag(self._language_option_tag_model.is_selected,
            self._language_option_tag_model.language_code_name, self._language_option_tag_model.display_language_name)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: LanguageOptionTagController self parameter.
        Returns:
            Returns show_language_option_tag().
        """
        return self.show_language_option_tag()
