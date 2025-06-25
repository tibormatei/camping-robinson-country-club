# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailerModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TrailerModel.
"""

import unittest
from app.models.rental_details import TrailerModel


class TestTrailerModel(unittest.TestCase):
    """
    @summary: TrailerModel tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestTrailerModel self parameter.
        """
        self.trailerModel = TrailerModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self):
        self.assertEqual(self.trailerModel.TrailerCapacity, '-')
        self.assertEqual(self.trailerModel.LeiPrice, 0)
        self.assertEqual(self.trailerModel.EurPrice, 0)

    # Test TrailerCapacity
    def test_02_TrailerCapacity(self):
        TRAILER_CAPACITY = '2-3 pers.'
        self.trailerModel.TrailerCapacity = TRAILER_CAPACITY
        self.assertEqual(self.trailerModel.TrailerCapacity, TRAILER_CAPACITY)

    # Test LeiPrice
    def test_03_LeiPrice(self):
        LEI_PRICE = 200
        self.trailerModel.LeiPrice = LEI_PRICE
        self.assertEqual(self.trailerModel.LeiPrice, LEI_PRICE)

    # Test EurPrice
    def test_04_EurPrice(self):
        EUR_PRICE = 40
        self.trailerModel.EurPrice = EUR_PRICE
        self.assertEqual(self.trailerModel.EurPrice, EUR_PRICE)

if __name__ == '__main__':
    unittest.main()
