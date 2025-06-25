# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_LanguageOptionTagController.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TrailerView.
"""

import unittest

from app.models.header_languages import LanguageOptionTagModel
from app.models.header_languages import LanguageOptionTagsModel
from app.views.header_languages import LanguageOptionTagsView
from app.controllers.header_languages import LanguageOptionTagsController

class TestLanguageOptionTagController(unittest.TestCase):
    """
    @summary: TestLanguageOptionTagController tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestLanguageOptionTagController self parameter.
        """
        en = LanguageOptionTagModel('English', 'en', True)
        hu = LanguageOptionTagModel('Hungarian', 'hu')
        langList = list()
        langList.append(en)
        langList.append(hu)

        languageOptionTagsModel = LanguageOptionTagsModel(langList)
        languageOptionTagsView = LanguageOptionTagsView()
        self.languageOptionTagController = LanguageOptionTagsController(languageOptionTagsModel, languageOptionTagsView)

    # Pozitiv tests:
    # Test showLanguageOptionTags method
    def test_01_showLanguageOptionTags(self):
        EXPECTED_RESULT: str = ('<option selected value="en">English</option>\n'
                                '<option value="hu">Hungarian</option>\n')

        self.assertEqual(self.languageOptionTagController.showLanguageOptionTags(), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
