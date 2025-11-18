# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the language option tags model and view.
"""

from models.header_languages import LanguageOptionTagsModel


class LanguageOptionTagsController():
    """
    This class controller the language option tags details.
    """

    def __init__(self, language_option_tags_model: LanguageOptionTagsModel, language_option_tags_view):
        """
        The init method initialize instance attributes.

        Args:
            self: LanguageOptionTagsController self parameter.
            language_option_tags_model: The model class for MVC pattern.
            language_option_tags_view: The view class for MVC pattern.
        """
        self._language_option_tags_model: LanguageOptionTagsModel = language_option_tags_model
        from views.header_languages import LanguageOptionTagsView
        self._language_option_tags_view: LanguageOptionTagsView = language_option_tags_view

    def show_language_option_tags(self) -> str:
        """
        Return the view of tent.

        Args:
            self: LanguageOptionTagsController self parameter.
        Returns:
            Returns view of Language Option Tags in string.
        """
        return self._language_option_tags_view.show_language_option_tags(self._language_option_tags_model.language_option_tag_models)

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: LanguageOptionTagsController self parameter.
        Returns:
            Returns show_language_option_tags().
        """
        return self.show_language_option_tags()
