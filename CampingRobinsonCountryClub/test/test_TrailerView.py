# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailerView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TrailerView.
"""

import unittest
from app.views.rental_details import TrailerView


class TestTrailerView(unittest.TestCase):
    """
    TestTrailerView tests.
    """

    def setUp(self):
        """
        Fresh instance for each test.

        Args:
            self: TestTrailerView self parameter.
        """
        self.trailer_view = TrailerView()

    # Pozitiv tests:
    # Test show_trailer_view method
    def test_01_show_trailer_view(self):
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

        self.assertEqual(self.trailer_view.show_trailer_view(TRANSLATIONS, TRAILER_CAPACITY, LEI_PRICE, EUR_PRICE), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
