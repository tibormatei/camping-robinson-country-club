# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model for the option tags in the header language select.
"""

from models.header_languages import LanguageOptionTagModel


class LanguageOptionTagsModel():
    """
    @summary: This class is a model of language option tags.
    """

    def __init__(self, languageOptionTagModels: list[LanguageOptionTagModel]):
        """
        @summary: The init method initialize instance attributes.
        @param self: LanguageOptionTagsModel self parameter.
        @param languageOptionTagModels: A list with LanguageOptionTagModels.
        """
        self._languageOptionTagModels: list[LanguageOptionTagModel] = languageOptionTagModels

    @property
    def LanguageOptionTagModels(self) -> list[LanguageOptionTagModel]:
        """
        @summary: The DisplayLanguageName getter property.
        @param self: LanguageOptionTagsModel self parameter.
        @returns: Language name.
        """
        return self._languageOptionTagModels
