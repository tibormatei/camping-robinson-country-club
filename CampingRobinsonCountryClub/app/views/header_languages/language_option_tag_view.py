# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of language option tag.
"""


class LanguageOptionTagView():
    """
    @summary: This class handles the view of language option tag.
    """

    def __init__(self):
        """
        @summary: Language Option Tag view.
        @param self: LanguageOptionTagView self parameter.
        """
        pass

    @classmethod
    def showLanguageOptionTag(cls, selected: bool, value: str, displayLanguageName: str) -> str:
        """
        @summary: Create the full language option tag view.
        @param cls: LanguageOptionTagView cls parameter.
        @param selected: option tag is selected.
        @param value: Value property value.
        @param displayLanguageName: Display Language Name.
        @returns: Returns a full displayable option html tag Exp: <option selected value="ro">Romanian</option>.
        """
        optionTag: str = '<option'

        # selected option:
        if selected == True:
            optionTag += ' selected'

        # value property:
        valueProperty: str = f" value=\"{value}\""
        optionTag += (valueProperty + '>')

        # inner html:
        optionTag += displayLanguageName

        # close option tag:
        optionTag += '</option>'

        return optionTag

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param cls: LanguageOptionTagView cls parameter.
        """
        return self.showLanguageOptionTag()
