# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_RentalDetailsDataFromFile.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TentModel.
"""

import unittest
from app.data import RentalDetailsDataFromFile


class TestRentalDetailsDataFromFile(unittest.TestCase):
    """
    RentalDetailsDataFromFile tests.
    """

    def setUp(self):
        """
        Fresh instance for each test

        Args:
            self: TestRentalDetailsDataFromFile self parameter.
        """
        self.rental_details_data_from_file = RentalDetailsDataFromFile()

    # Pozitiv tests:
    # Test get_tent_persons
    def test_01_get_tent_persons(self):
        EXPECTED_LIST: list[str] = ['1', '2-3', '4-5', '6 <']
        self.assertListEqual(self.rental_details_data_from_file.get_tent_persons(), EXPECTED_LIST)

    # Test get_tent_price_lei
    def test_02_get_tent_price_lei(self):
        EXPECTED_TENT_PRICE_LEI: int = 75
        self.assertEqual(self.rental_details_data_from_file.get_tent_price_lei(), EXPECTED_TENT_PRICE_LEI)

    # Test get_tent_price_eur
    def test_03_get_tent_price_eur(self):
        EXPECTED_TENT_PRICE_EUR: int = 15
        self.assertEqual(self.rental_details_data_from_file.get_tent_price_eur(), EXPECTED_TENT_PRICE_EUR)

    # Test get_trailer_capacities
    def test_04_get_trailer_capacities(self):
        EXPECTED_LIST: list[str] = ['1', '2-3', '4-5', '6<']
        self.assertListEqual(self.rental_details_data_from_file.get_trailer_capacities(), EXPECTED_LIST)

    # Test get_trailer_price_lei
    def test_05_get_trailer_price_lei(self):
        CAPACITY1: str = '1'
        EXPECTED_TRAILER_PRICE_LEI_200: int = 200
        self.assertEqual(self.rental_details_data_from_file.get_trailer_price_lei(CAPACITY1), EXPECTED_TRAILER_PRICE_LEI_200)

        CAPACITY45: str = '4-5'
        EXPECTED_TRAILER_PRICE_LEI_250: int = 250
        self.assertEqual(self.rental_details_data_from_file.get_trailer_price_lei(CAPACITY45), EXPECTED_TRAILER_PRICE_LEI_250)

    # Test get_trailer_price_eur
    def test_06_get_trailer_price_eur(self):
        CAPACITY1: str = '1'
        EXPECTED_TRAILER_PRICE_EUR_40: int = 40
        self.assertEqual(self.rental_details_data_from_file.get_trailer_price_eur(CAPACITY1), EXPECTED_TRAILER_PRICE_EUR_40)

        CAPACITY45: str = '4-5'
        EXPECTED_TRAILER_PRICE_EUR_50: int = 50
        self.assertEqual(self.rental_details_data_from_file.get_trailer_price_eur(CAPACITY45), EXPECTED_TRAILER_PRICE_EUR_50)

    # Test get_dog_price_lei
    def test_07_get_dog_price_lei(self):
        EXPECTED_DOG_PRICE_LEI: int = 25
        self.assertEqual(self.rental_details_data_from_file.get_dog_price_lei(), EXPECTED_DOG_PRICE_LEI)

    # Test get_dog_price_eur
    def test_08_get_dog_price_eur(self):
        EXPECTED_DOG_PRICE_EUR: int = 5
        self.assertEqual(self.rental_details_data_from_file.get_dog_price_eur(), EXPECTED_DOG_PRICE_EUR)
