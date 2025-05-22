# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_DogModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of DogModel.
"""

import unittest
from app.models import DogModel


class TestDogModel(unittest.TestCase) :
    """
    @summary: DogModel tests.
    """

    def setUp(self) :
        """
        @summary: Fresh instance for each test
        @param self: TestTentModel self parameter.
        """
        self.dogModel = DogModel()

    # Pozitiv tests:
    # Test basic constructor
    def test_01_basic_values(self) :
        self.assertEqual(self.dogModel.LeiPricePerNight, 0)
        self.assertEqual(self.dogModel.EurPricePerNight, 0)

    # Test LeiPricePerNight
    def test_02_LeiPricePerNight(self) :
        LEI_PRICE_PER_NIGHT = 25
        self.dogModel.LeiPricePerNight = LEI_PRICE_PER_NIGHT
        self.assertEqual(self.dogModel.LeiPricePerNight, LEI_PRICE_PER_NIGHT)

    # Test EurPricePerNight
    def test_03_EurPricePerNight(self) :
        EUR_PRICE_PER_NIGHT = 5
        self.dogModel.EurPricePerNight = EUR_PRICE_PER_NIGHT
        self.assertEqual(self.dogModel.EurPricePerNight, EUR_PRICE_PER_NIGHT)

if __name__ == '__main__':
    unittest.main()
