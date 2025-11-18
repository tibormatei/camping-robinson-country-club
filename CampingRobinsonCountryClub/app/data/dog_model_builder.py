# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class returns the TentModel with dates.
"""

from data import RentalDetailsDataAccess
from models.rental_details import DogModel


class DogModelBuilder():
    """
    This class returns the DogModel with dates.
    """

    def __init__(self, data_access: RentalDetailsDataAccess):
        """
        The init method initialize instance attributes.

        Args:
            self: DogModelBuilder self parameter.
            data_access: RentalDetailsDataAccess's inheritance class.
        """
        self._data_access = data_access

    def retrive_dog_model(self) -> DogModel:
        """
        Retrive DogModel with dates.

        Args:
            self: DogModelBuilder self parameter.
        Returns:
            Returns the DogModel with dates.
        """
        lei_price_per_night: int = self._data_access.get_dog_price_lei()
        eur_price_per_night: int = self._data_access.get_dog_price_eur()
        dog_model: DogModel = DogModel(lei_price_per_night, eur_price_per_night)

        return dog_model
