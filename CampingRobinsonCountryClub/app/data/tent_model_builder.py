# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class returns the TentModel with dates.
"""

from data import RentalDetailsDataAccess
from models.rental_details import TentModel


class TentModelBuilder():
    """
    This class returns the TentModel with dates.
    """

    def __init__(self, data_access: RentalDetailsDataAccess):
        """
        The init method initialize instance attributes.

        Args:
            self: TentModelBuilder self parameter.
            data_access: RentalDetailsDataAccess's inheritance class.
        """
        self._data_access = data_access

    def retrive_tent_model(self) -> TentModel:
        """
        Retrive TentModel with dates.

        Args:
            self: TentModelBuilder self parameter.
        Returns:
            Returns the TentModel with dates.
        """
        tent_capacities: list[str] = self._data_access.get_tent_persons()
        lei_price_per_person: int = self._data_access.get_tent_price_lei()
        eur_price_per_person: int = self._data_access.get_tent_price_eur()
        tent_model: TentModel = TentModel(tent_capacities, lei_price_per_person, eur_price_per_person)

        return tent_model
