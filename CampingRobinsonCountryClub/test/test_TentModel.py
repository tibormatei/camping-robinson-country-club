# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TentModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TentModel.
"""

import unittest
from app.models.rental_details import TentModel


class TestTentModel(unittest.TestCase):
    """
    TentModel tests.
    """

    def setUp(self):
        """
        Fresh instance for each test

        Args:
            self: TestTentModel self parameter.
        """
        self.tent_model = TentModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self):
        self.assertEqual(len(self.tent_model.tent_capacities), 0)
        self.assertEqual(self.tent_model.lei_price_per_person, 0)
        self.assertEqual(self.tent_model.eur_price_per_person, 0)

    # Test lei_price_per_person
    def test_02_lei_price_per_person(self):
        LEI_PRICE_PER_PERSON = 75
        self.tent_model.lei_price_per_person = LEI_PRICE_PER_PERSON
        self.assertEqual(self.tent_model.lei_price_per_person, LEI_PRICE_PER_PERSON)

    # Test eur_price_per_person
    def test_03_eur_price_per_person(self):
        EUR_PRICE_PER_PERSON = 15
        self.tent_model.eur_price_per_person = EUR_PRICE_PER_PERSON
        self.assertEqual(self.tent_model.eur_price_per_person, EUR_PRICE_PER_PERSON)

    # Test add_tent_capacity
    def test_04_add_tent_capacity(self):
        TENT_CAPACITY_2_3 = "2-3"
        self.tent_model.add_tent_capacity(TENT_CAPACITY_2_3)
        self.assertEqual(len(self.tent_model.tent_capacities), 1)

if __name__ == '__main__':
    unittest.main()
