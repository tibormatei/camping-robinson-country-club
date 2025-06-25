# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_controller.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the language option tags model and view.
"""

from models.header_languages import LanguageOptionTagsModel


class LanguageOptionTagsController():
    """
    @summary: This class controller the language option tags details.
    """

    def __init__(self, languageOptionTagsModel: LanguageOptionTagsModel, languageOptionTagsView):
        """
        @summary: The init method initialize instance attributes.
        @param self: LanguageOptionTagsController self parameter.
        @param languageOptionTagsModel: The model class for MVC pattern.
        @param languageOptionTagsView: The view class for MVC pattern.
        """
        self._languageOptionTagsModel: LanguageOptionTagsModel = languageOptionTagsModel
        from views.header_languages import LanguageOptionTagsView
        self._languageOptionTagsView: LanguageOptionTagsView = languageOptionTagsView

    def showLanguageOptionTags(self) -> str:
        """
        @summary: Return the view of tent.
        @param self: LanguageOptionTagsController self parameter.
        @returns: Returns view of Language Option Tags in string.
        """
        return self._languageOptionTagsView.showLanguageOptionTags(self._languageOptionTagsModel.LanguageOptionTagModels)

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: LanguageOptionTagsController self parameter.
        @returns: Returns showLanguageOptionTag().
        """
        return self.showLanguageOptionTags()
