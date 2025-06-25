# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model for the option tag in the header language select.
"""


class LanguageOptionTagModel():
    """
    @summary: This class is a model of language option tag.
    """

    def __init__(self, displayLanguageName: str = '', languageCodeName: str = '', selected: bool = False):
        """
        @summary: The init method initialize instance attributes.
        @param self: LanguageOptionTagModel self parameter.
        @param displayLanguageName: Display Language Name the inner text.
        @param languageCodeName: value parameter.
        @param selected: Is selected option.
        """
        self._displayLanguageName: str = displayLanguageName
        self._languageCodeName: str = languageCodeName
        self._selected: bool = selected

    @property
    def DisplayLanguageName(self) -> str:
        """
        @summary: The DisplayLanguageName getter property.
        @param self: LanguageOptionTagModel self parameter.
        @returns: Language name.
        """
        return self._displayLanguageName

    @property
    def LanguageCodeName(self) -> str:
        """
        @summary: The LanguageCodeName getter property.
        @param self: LanguageOptionTagModel self parameter.
        @returns: Language code naem for value parameter.
        """
        return self._languageCodeName

    @property
    def IsSelected(self) -> bool:
        """
        @summary: The Selected getter property.
        @param self: LanguageOptionTagModel self parameter.
        @returns: Return True if the option is selected.
        """
        return self._selected
