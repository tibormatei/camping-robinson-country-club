# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: language_options_for_select.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class controller the Language Options For Select details.
"""

from models.header_languages import LanguageOptionTagModel
from models.header_languages import LanguageOptionTagsModel
from views.header_languages import LanguageOptionTagsView
from controllers.header_languages import LanguageOptionTagsController
from utils.language import LanguageCodes


class LanguageOptionsForSelect():
    """
    This class controller the language options for select objects.
    """

    def __init__(self, selected_language_code: str):
        """
        The init method initialize instance attributes.

        Args:
            self: LanguageOptionsForSelect self parameter.
            selected_language_code: An language code.
        """
        language_option_tag_models = list()
        for l in LanguageCodes:
            if l.name == selected_language_code:
                language_option_tag_model = LanguageOptionTagModel(l.value, l.name, True)
            else:
                language_option_tag_model = LanguageOptionTagModel(l.value, l.name, False)
            language_option_tag_models.append(language_option_tag_model)

        language_option_tags_model = LanguageOptionTagsModel(language_option_tag_models)
        language_option_tags_view = LanguageOptionTagsView()
        self._language_option_tags_controller = LanguageOptionTagsController(language_option_tags_model, language_option_tags_view)

    def generate_language_options_for_select(self) -> str:
        """
        The method build all option tag for select tag.

        Args:
            self: LanguageOptionsForSelect self parameter.
        Returns:
            html code piece.
        """
        return self._language_option_tags_controller.show_language_option_tags()
