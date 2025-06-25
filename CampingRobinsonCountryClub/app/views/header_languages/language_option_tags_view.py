# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of language option tags.
"""

from models.header_languages import LanguageOptionTagModel
from views.header_languages import LanguageOptionTagView
from controllers.header_languages import LanguageOptionTagController


class LanguageOptionTagsView():
    """
    @summary: This class handles the view of language option tags.
    """

    def __init__(self):
        """
        @summary: Language Option Tags view.
        @param self: LanguageOptionTagsView self parameter.
        """
        self._languageOptionTagView = LanguageOptionTagView()

    def showLanguageOptionTags(self, languageOptionTags: list[LanguageOptionTagModel]) -> str:
        """
        @summary: Create the full language option tag view.
        @param cls: LanguageOptionTagsView cls parameter.
        @param languageOptionTags: All LanguageOptionTagModel in a list.
        @returns: Returns a full displayable option html tags.
        """
        optionTags: str = ''

        for anguageOptionTagModel in languageOptionTags:
            languageOptionTagController = LanguageOptionTagController(anguageOptionTagModel, self._languageOptionTagView)
            optionTags += languageOptionTagController.showLanguageOptionTag()
            optionTags += '\n'

        return optionTags

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: LanguageOptionTagsView cls parameter.
        """
        return self.showLanguageOptionTags()
