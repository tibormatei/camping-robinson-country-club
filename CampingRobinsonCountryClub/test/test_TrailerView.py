# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailerView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TrailerView.
"""

import unittest
from app.views import TrailerView


class TestTrailerView(unittest.TestCase):
    """
    @summary: TestTrailerView tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestTrailerView self parameter.
        """
        self.trailerView = TrailerView()

    # Pozitiv tests:
    # Test showTrailerView method
    def test_01_showTrailerView(self):
        EXPECTED_RESULT: str = '<tr><td>2-3 Person</td><td>200</td><td>50</td></tr>'

        TRANSLATIONS: dict = {
            "rentalDetails": {
                "trailerDetails": {
                    "personHeader": "Camper Trailer",
                    "lei": "Lei",
                    "eur": "Eur",
                    "personName": "Person"
                }
            }
        }
        TRAILER_CAPACITY: str = "2-3"
        LEI_PRICE: int = 200
        EUR_PRICE: int = 50

        self.assertEqual(self.trailerView.showTrailerView(TRANSLATIONS, TRAILER_CAPACITY, LEI_PRICE, EUR_PRICE), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
