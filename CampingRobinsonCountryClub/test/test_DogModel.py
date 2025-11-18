# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_DogModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of DogModel.
"""

import unittest
from app.models.rental_details import DogModel


class TestDogModel(unittest.TestCase):
    """
    DogModel tests.
    """

    def setUp(self):
        """
        Fresh instance for each test

        Args:
            self: TestTentModel self parameter.
        """
        self.dog_model = DogModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self):
        self.assertEqual(self.dog_model.lei_price_per_night, 0)
        self.assertEqual(self.dog_model.eur_price_per_night, 0)

    # Test lei_price_per_night
    def test_02_lei_price_per_night(self):
        LEI_PRICE_PER_NIGHT = 25
        self.dog_model.lei_price_per_night = LEI_PRICE_PER_NIGHT
        self.assertEqual(self.dog_model.lei_price_per_night, LEI_PRICE_PER_NIGHT)

    # Test eur_price_per_night
    def test_03_eur_price_per_night(self):
        EUR_PRICE_PER_NIGHT = 5
        self.dog_model.eur_price_per_night = EUR_PRICE_PER_NIGHT
        self.assertEqual(self.dog_model.eur_price_per_night, EUR_PRICE_PER_NIGHT)

if __name__ == '__main__':
    unittest.main()
