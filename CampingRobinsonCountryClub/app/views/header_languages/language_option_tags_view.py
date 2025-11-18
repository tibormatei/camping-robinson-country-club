# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of language option tags.
"""

from models.header_languages import LanguageOptionTagModel
from views.header_languages import LanguageOptionTagView
from controllers.header_languages import LanguageOptionTagController


class LanguageOptionTagsView():
    """
    This class handles the view of language option tags.
    """

    def __init__(self):
        """
        Language Option Tags view.

        Args:
            self: LanguageOptionTagsView self parameter.
        """
        self._language_option_tag_view = LanguageOptionTagView()

    def show_language_option_tags(self, language_option_tags: list[LanguageOptionTagModel]) -> str:
        """
        Create the full language option tag view.

        Args:
            cls: LanguageOptionTagsView cls parameter.
            language_option_tags: All LanguageOptionTagModel in a list.
        Returns:
            Returns a full displayable option html tags.
        """
        option_tags: str = ''

        for language_option_tag_model in language_option_tags:
            language_option_tag_controller = LanguageOptionTagController(language_option_tag_model, self._language_option_tag_view)
            option_tags += language_option_tag_controller.show_language_option_tag()
            option_tags += '\n'

        return option_tags

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            cls: LanguageOptionTagsView cls parameter.
        """
        return self.show_language_option_tags()
