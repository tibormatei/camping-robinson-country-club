# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the language option tag model and view.
"""

from models.header_languages import LanguageOptionTagModel
from views.header_languages import LanguageOptionTagView


class LanguageOptionTagController():
    """
    @summary: This class controller the language option tag details.
    """

    def __init__(self, languageOptionTagModel: LanguageOptionTagModel, languageOptionTagView: LanguageOptionTagView):
        """
        @summary: The init method initialize instance attributes.
        @param self: LanguageOptionTagController self parameter.
        @param languageOptionTagModel: The model class for MVC pattern.
        @param languageOptionTagView: The view class for MVC pattern.
        """
        self._languageOptionTagModel: LanguageOptionTagModel = languageOptionTagModel
        self._languageOptionTagView: LanguageOptionTagView = languageOptionTagView

    def showLanguageOptionTag(self) -> str:
        """
        @summary: Return the view of tent.
        @param self: LanguageOptionTagController self parameter.
        @returns: Returns view of Language Option Tag in string.
        """
        return self._languageOptionTagView.showLanguageOptionTag(self._languageOptionTagModel.IsSelected,
            self._languageOptionTagModel.LanguageCodeName, self._languageOptionTagModel.DisplayLanguageName)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: LanguageOptionTagController self parameter.
        @returns: Returns showLanguageOptionTag().
        """
        return self.showLanguageOptionTag()
