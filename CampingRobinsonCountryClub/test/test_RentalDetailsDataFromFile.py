# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_RentalDetailsDataFromFile.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TentModel.
"""

import unittest
from app.data import RentalDetailsDataFromFile


class TestRentalDetailsDataFromFile(unittest.TestCase):
    """
    @summary: RentalDetailsDataFromFile tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestRentalDetailsDataFromFile self parameter.
        """
        self.rentalDetailsDataFromFile = RentalDetailsDataFromFile()

    # Pozitiv tests:
    # Test getTentPersons
    def test_01_getTentPersons(self):
        EXPECTED_LIST: list[str] = ['1', '2-3', '4-5', '6 <']
        self.assertListEqual(self.rentalDetailsDataFromFile.getTentPersons(), EXPECTED_LIST)

    # Test getTentPriceLei
    def test_02_getTentPriceLei(self):
        EXPECTED_TENT_PRICE_LEI: int = 75
        self.assertEqual(self.rentalDetailsDataFromFile.getTentPriceLei(), EXPECTED_TENT_PRICE_LEI)

    # Test getTentPriceEur
    def test_03_getTentPriceEur(self):
        EXPECTED_TENT_PRICE_EUR: int = 15
        self.assertEqual(self.rentalDetailsDataFromFile.getTentPriceEur(), EXPECTED_TENT_PRICE_EUR)

    # Test getTrailerCapacity
    def test_04_getTrailerCapacity(self):
        EXPECTED_LIST: list[str] = ['1', '2-3', '4-5', '6<']
        self.assertListEqual(self.rentalDetailsDataFromFile.getTrailerCapacities(), EXPECTED_LIST)

    # Test getTrailerPriceLei
    def test_05_getTrailerPriceLei(self):
        CAPACITY1: str = '1'
        EXPECTED_TRAILER_PRICE_LEI_200: int = 200
        self.assertEqual(self.rentalDetailsDataFromFile.getTrailerPriceLei(CAPACITY1), EXPECTED_TRAILER_PRICE_LEI_200)

        CAPACITY45: str = '4-5'
        EXPECTED_TRAILER_PRICE_LEI_250: int = 250
        self.assertEqual(self.rentalDetailsDataFromFile.getTrailerPriceLei(CAPACITY45), EXPECTED_TRAILER_PRICE_LEI_250)

    # Test getTrailerPriceEur
    def test_06_getTrailerPriceEur(self):
        CAPACITY1: str = '1'
        EXPECTED_TRAILER_PRICE_EUR_40: int = 40
        self.assertEqual(self.rentalDetailsDataFromFile.getTrailerPriceEur(CAPACITY1), EXPECTED_TRAILER_PRICE_EUR_40)

        CAPACITY45: str = '4-5'
        EXPECTED_TRAILER_PRICE_EUR_50: int = 50
        self.assertEqual(self.rentalDetailsDataFromFile.getTrailerPriceEur(CAPACITY45), EXPECTED_TRAILER_PRICE_EUR_50)

    # Test getDogPriceLei
    def test_07_getDogPriceLei(self):
        EXPECTED_DOG_PRICE_LEI: int = 25
        self.assertEqual(self.rentalDetailsDataFromFile.getDogPriceLei(), EXPECTED_DOG_PRICE_LEI)

    # Test getDogPriceEur
    def test_08_getDogPriceEur(self):
        EXPECTED_DOG_PRICE_EUR: int = 5
        self.assertEqual(self.rentalDetailsDataFromFile.getDogPriceEur(), EXPECTED_DOG_PRICE_EUR)
