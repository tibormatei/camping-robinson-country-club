# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_DogView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TrailerView.
"""

import unittest
from app.views.rental_details import DogView


class TestDogView(unittest.TestCase):
    """
    TestDogView tests.
    """

    def setUp(self):
        """
        Fresh instance for each test

        Args:
            self: TestDogView self parameter.
        """
        self.dog_view = DogView()

    # Pozitiv tests:
    # Test show_dog_view method
    def test_01_show_dog_view(self):
        EXPECTED_RESULT: str = ('<table id="rentaldetails-dog-table" class="rentaldetails-table">\n'
                                '    <thead>\n'
                                '        <tr>\n'
                                '            <th id="rentaldetails-dog-table-thead-dogheader"></th>\n'
                                '            <th id="rentaldetails-dog-table-thead-lei">Lei</th>\n'
                                '            <th id="rentaldetails-dog-table-thead-eur">Eur</th>\n'
                                '        </tr>\n'
                                '    </thead>\n'
                                '    <tbody>\n'
                                '        <tr><td>Dog</td><td>50 / Night</td><td>10 / Night</td></tr>\n'
                                '    </tbody>\n'
                                '</table>')

        TRANSLATIONS: dict = {
            "rentalDetails": {
                "dogDetails": {
                    "dog": "Dog",
                    "lei": "Lei",
                    "eur": "Eur",
                    "priceDetail": " / Night"
                }
            }
        }
        LEI_PRICE_PER_NIGHT: int = 50
        EUR_PRICE_PER_NIGHT: int = 10

        self.assertEqual(self.dog_view.show_dog_view(TRANSLATIONS, LEI_PRICE_PER_NIGHT, EUR_PRICE_PER_NIGHT), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
