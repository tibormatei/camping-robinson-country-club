# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_options_for_select.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class controller the Language Options For Select details.
"""

from models.header_languages import LanguageOptionTagModel
from models.header_languages import LanguageOptionTagsModel
from views.header_languages import LanguageOptionTagsView
from controllers.header_languages import LanguageOptionTagsController
from utils.language import LanguageCodes


class LanguageOptionsForSelect():
    """
    @summary: This class controller the language options for select objects.
    """

    def __init__(self, selectedLanguageCode: str):
        """
        @summary: The init method initialize instance attributes.
        @param self: LanguageOptionsForSelect self parameter.
        """
        languageOptionTagModels = list()
        for l in LanguageCodes:
            if l.name == selectedLanguageCode:
                languageOptionTagModel = LanguageOptionTagModel(l.value, l.name, True)
            else:
                languageOptionTagModel = LanguageOptionTagModel(l.value, l.name, False)
            languageOptionTagModels.append(languageOptionTagModel)

        languageOptionTagsModel = LanguageOptionTagsModel(languageOptionTagModels)
        languageOptionTagsView = LanguageOptionTagsView()
        self._languageOptionTagsController = LanguageOptionTagsController(languageOptionTagsModel, languageOptionTagsView)

    def generateLanguageOptionsForSelect(self) -> str:
        """
        @summary: The method build all option tag for select tag.
        @param self: LanguageOptionsForSelect self parameter.
        @param path: Pice of html code.
        """
        return self._languageOptionTagsController.showLanguageOptionTags()
