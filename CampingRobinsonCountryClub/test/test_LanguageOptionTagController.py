# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_LanguageOptionTagController.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TrailerView.
"""

import unittest

from app.models.header_languages import LanguageOptionTagModel
from app.models.header_languages import LanguageOptionTagsModel
from app.views.header_languages import LanguageOptionTagsView
from app.controllers.header_languages import LanguageOptionTagsController

class TestLanguageOptionTagController(unittest.TestCase):
    """
    TestLanguageOptionTagController tests.
    """

    def setUp(self):
        """
        Fresh instance for each test.

        Args:
            self: TestLanguageOptionTagController self parameter.
        """
        en = LanguageOptionTagModel('English', 'en', True)
        hu = LanguageOptionTagModel('Hungarian', 'hu')
        lang_list = list()
        lang_list.append(en)
        lang_list.append(hu)

        language_option_tags_model = LanguageOptionTagsModel(lang_list)
        language_option_tags_view = LanguageOptionTagsView()
        self.language_option_tag_controller = LanguageOptionTagsController(language_option_tags_model, language_option_tags_view)

    # Pozitiv tests:
    # Test show_language_option_tags method
    def test_01_show_language_option_tags(self):
        EXPECTED_RESULT: str = ('<option selected value="en">English</option>\n'
                                '<option value="hu">Hungarian</option>\n')

        self.assertEqual(self.language_option_tag_controller.show_language_option_tags(), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
