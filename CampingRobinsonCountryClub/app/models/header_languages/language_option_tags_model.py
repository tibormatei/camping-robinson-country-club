# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tags_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model for the option tags in the header language select.
"""

from models.header_languages import LanguageOptionTagModel


class LanguageOptionTagsModel():
    """
    This class is a model of language option tags.
    """

    def __init__(self, language_option_tag_models: list[LanguageOptionTagModel]):
        """
        The init method initialize instance attributes.

        Args:
            self: LanguageOptionTagsModel self parameter.
            language_option_tag_models: A list with LanguageOptionTagModels.
        """
        self._language_option_tag_models: list[LanguageOptionTagModel] = language_option_tag_models

    @property
    def language_option_tag_models(self) -> list[LanguageOptionTagModel]:
        """
        The language_option_tag_models getter property.

        Args:
            self: LanguageOptionTagsModel self parameter.
        Returns:
            Language name.
        """
        return self._language_option_tag_models
