# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailerModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TrailerModel.
"""

import unittest
from app.models.rental_details import TrailerModel


class TestTrailerModel(unittest.TestCase):
    """
    TrailerModel tests.
    """

    def setUp(self):
        """
        Fresh instance for each test.

        Args:
            self: TestTrailerModel self parameter.
        """
        self.trailerModel = TrailerModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self):
        self.assertEqual(self.trailerModel.trailer_capacity, '-')
        self.assertEqual(self.trailerModel.lei_price, 0)
        self.assertEqual(self.trailerModel.eur_price, 0)

    # Test trailer_capacity
    def test_02_trailer_capacity(self):
        TRAILER_CAPACITY = '2-3 pers.'
        self.trailerModel.trailer_capacity = TRAILER_CAPACITY
        self.assertEqual(self.trailerModel.trailer_capacity, TRAILER_CAPACITY)

    # Test lei_price
    def test_03_lei_price(self):
        LEI_PRICE = 200
        self.trailerModel.lei_price = LEI_PRICE
        self.assertEqual(self.trailerModel.lei_price, LEI_PRICE)

    # Test eur_price
    def test_04_eur_price(self):
        EUR_PRICE = 40
        self.trailerModel.eur_price = EUR_PRICE
        self.assertEqual(self.trailerModel.eur_price, EUR_PRICE)

if __name__ == '__main__':
    unittest.main()
