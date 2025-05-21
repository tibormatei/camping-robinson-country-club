# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TentModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TentModel.
"""

import unittest
from app.models import TentModel


class TestTentModel(unittest.TestCase):
    """
    @summary: TentModel tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
         @param self: TestTentModel self parameter.
        """
        self.tentModel = TentModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self):
        self.assertEqual(len(self.tentModel.TentCapacities), 0)
        self.assertEqual(self.tentModel.LeiPricePerPerson, 0)
        self.assertEqual(self.tentModel.EurPricePerPerson, 0)

    # Test LeiPricePerPerson
    def test_02_LeiPricePerPerson(self):
        LEI_PRICE_PER_PERSON = 75
        self.tentModel.LeiPricePerPerson = LEI_PRICE_PER_PERSON
        self.assertEqual(self.tentModel.LeiPricePerPerson, LEI_PRICE_PER_PERSON)

    # Test EurPricePerPerson
    def test_03_EurPricePerPerson(self):
        EUR_PRICE_PER_PERSON = 15
        self.tentModel.EurPricePerPerson = EUR_PRICE_PER_PERSON
        self.assertEqual(self.tentModel.EurPricePerPerson, EUR_PRICE_PER_PERSON)

    # Test AddTentCapacity
    def test_04_AddTentCapacity(self):
        TENT_CAPACITY_2_3 = "2-3"
        self.tentModel.AddTentCapacity(TENT_CAPACITY_2_3)
        self.assertEqual(len(self.tentModel.TentCapacities), 1)

if __name__ == '__main__':
    unittest.main()
