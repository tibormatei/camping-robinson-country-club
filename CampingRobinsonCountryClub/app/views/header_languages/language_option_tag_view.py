# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_option_tag_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of language option tag.
"""


class LanguageOptionTagView():
    """
    This class handles the view of language option tag.
    """

    def __init__(self):
        """
        Language Option Tag view.

        Args:
            self: LanguageOptionTagView self parameter.
        """
        pass

    @classmethod
    def show_language_option_tag(cls, selected: bool, value: str, display_language_name: str) -> str:
        """
        Create the full language option tag view.

        Args:
            cls: LanguageOptionTagView cls parameter.
            selected: option tag is selected.
            value: Value property value.
            display_language_name: Display Language Name.
        Returns:
            Returns a full displayable option html tag Exp: <option selected value="ro">Romanian</option>.
        """
        option_tag: str = '<option'

        # selected option:
        if selected == True:
            option_tag += ' selected'

        # value property:
        value_property: str = f" value=\"{value}\""
        option_tag += (value_property + '>')

        # inner html:
        option_tag += display_language_name

        # close option tag:
        option_tag += '</option>'

        return option_tag

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            cls: LanguageOptionTagView cls parameter.
        """
        return self.show_language_option_tag()
