# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TentModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of  TentModel.
"""

import unittest
from app.models.TentModel import TentModel


class TestTentModel(unittest.TestCase) :
    """
    @summary: TentModel tests.
    """

    def setUp(self) :
        """
        @summary: Fresh instance for each test
         @param self: TestTentModel self parameter.
        """
        self.tentModel = TentModel()

    # Test basic constructor.
    def test_basic_values(self) :
        self.assertEqual(self.tentModel.TentCapacities, [])
        self.assertEqual(self.tentModel.LeiPricePerPerson, 0)
        self.assertEqual(self.tentModel.EurPricePerPerson, 0)

if __name__ == '__main__':
    unittest.main()
