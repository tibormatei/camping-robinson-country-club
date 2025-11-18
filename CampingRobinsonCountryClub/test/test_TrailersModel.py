# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: test_TrailersModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class tests the functions of TrailersModel.
"""

import unittest
from app.models.rental_details import TrailerModel
from app.models.rental_details import TrailersModel


class TestTrailersModel(unittest.TestCase):
    """
    TrailersModel tests.
    """

    def setUp(self):
        """
        Fresh instance for each test

        Args:
            self: TestTrailersModel self parameter.
        """
        self.trailers_model = TrailersModel()

    # Pozitiv tests:
    # Test for add_trailer_model and the class is iterable.
    def test_01_add_trailer_model_and_can_iterable(self):
        TRAIL1 = TrailerModel('1 pers', 200, 40)
        TRAIL2 = TrailerModel('2-3 pers', 200, 40)
        self.trailers_model.add_trailer_model(TRAIL1)
        self.trailers_model.add_trailer_model(TRAIL2)

        n = 0
        for trail in self.trailers_model:
            self.assertIsNotNone(trail)
            n += 1
        
        self.assertEqual(n, 2)

if __name__ == '__main__':
    unittest.main()
