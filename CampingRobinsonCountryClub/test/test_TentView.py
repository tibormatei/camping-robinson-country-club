# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TentView.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TentView.
"""

import unittest
from app.views.rental_details import TentView


class TestTentView(unittest.TestCase):
    """
    @summary: TestTentView tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestTentView self parameter.
        """
        self.tentView = TentView()

    # Pozitiv tests:
    # Test showTentView method
    def test_01_showTentView(self):
        EXPECTED_RESULT: str = ('<table id="rentaldetails-tent-table" class="rentaldetails-table">\n'
                                '    <thead>\n'
                                '        <tr>\n'
                                '            <th id="rentaldetails-tent-table-thead-personheader">Tent</th>\n'
                                '            <th id="rentaldetails-tent-table-thead-lei">Lei / Person</th>\n'
                                '            <th id="rentaldetails-tent-table-thead-eur">Eur / Person</th>\n'
                                '        </tr>\n'
                                '    </thead>\n'
                                '    <tbody>\n'
                                '        <tr><td>1 Person</td><td rowspan="4">200</td><td rowspan="4">50</td></tr><tr><td>2-3 Person</td></tr><tr><td>4-5 Person</td></tr><tr><td>6 < Person</td></tr>\n'
                                '    </tbody>\n'
                                '</table>')

        TRANSLATIONS: dict = {
            "rentalDetails": {
                "tentDetails": {
                    "personHeader": "Tent",
                    "lei": "Lei",
                    "eur": "Eur",
                    "priceDetail": " / Person",
                    "personName": "Person"
                }
            }
        }
        TENT_CAPACITIES: list[str] = ['1', '2-3', '4-5', '6 <']
        LEI_PRICE_PER_PERSON: int = 200
        EUR_PRICE_PER_PERSON: int = 50

        self.assertEqual(self.tentView.showTentView(TRANSLATIONS, TENT_CAPACITIES, LEI_PRICE_PER_PERSON, EUR_PRICE_PER_PERSON), EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
