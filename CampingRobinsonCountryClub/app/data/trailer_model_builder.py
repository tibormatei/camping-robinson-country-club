# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class returns the TrailerModel with dates.
"""

from data import RentalDetailsDataAccess
from models.rental_details import TrailerModel


class TrailerModelBuilder():
    """
    This class returns the TrailerModel with dates.
    """

    def __init__(self, data_access: RentalDetailsDataAccess):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailerModelBuilder self parameter.
            data_access: RentalDetailsDataAccess's inheritance class.
        """
        self._data_access = data_access

    def retrive_trailer_model(self, trailer_capacity: str) -> TrailerModel:
        """
        Retrive TrailerModel with dates.

        Args:
            self: TrailerModelBuilder self parameter.
        Returns:
            Returns the TrailerModel with dates.
        """
        lei_price = self._data_access.get_trailer_price_lei(trailer_capacity)
        eur_price = self._data_access.get_trailer_price_eur(trailer_capacity)
        trailer_model: TrailerModel = TrailerModel(trailer_capacity, lei_price, eur_price)

        return trailer_model
