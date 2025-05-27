# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailersModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class tests the functions of TrailersModel.
"""

import unittest
from app.models import TrailerModel
from app.models import TrailersModel


class TestTrailersModel(unittest.TestCase):
    """
    @summary: TrailersModel tests.
    """

    def setUp(self):
        """
        @summary: Fresh instance for each test
        @param self: TestTrailersModel self parameter.
        """
        self.trailersModel = TrailersModel()

    # Pozitiv tests:
    # Test for AddTrailerMode and the class is iterable.
    def test_01_AddTrailerModel_and_canIterable(self):
        TRAIL1 = TrailerModel('1 pers', 200, 40)
        TRAIL2 = TrailerModel('2-3 pers', 200, 40)
        self.trailersModel.AddTrailerModel(TRAIL1)
        self.trailersModel.AddTrailerModel(TRAIL2)

        n = 0
        for trail in self.trailersModel:
            self.assertIsNotNone(trail)
            n += 1
        
        self.assertEqual(n, 2)

if __name__ == '__main__':
    unittest.main()
