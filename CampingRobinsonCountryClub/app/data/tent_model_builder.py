# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class returns the TentModel with dates.
"""

from data import RentalDetailsDataAccess
from models.rental_details import TentModel


class TentModelBuilder():
    """
    @summary: This class returns the TentModel with dates.
    """

    def __init__(self, dataAccess: RentalDetailsDataAccess):
        """
        @summary: The init method initialize instance attributes.
        @param self: TentModelBuilder self parameter.
        @param sedataAccesslf: RentalDetailsDataAccess's inheritance class.
        """
        self._dataAccess = dataAccess

    def RetriveTentModel(self) -> TentModel:
        """
        @summary: Retrive TentModel with dates.
        @param self: TentModelBuilder self parameter.
        @returns: Returns the TentModel with dates.
        """
        tentCapacities: list[str] = self._dataAccess.getTentPersons()
        leiPricePerPerson: int = self._dataAccess.getTentPriceLei()
        eurPricePerPerson: int = self._dataAccess.getTentPriceEur()
        tentModel: TentModel = TentModel(tentCapacities, leiPricePerPerson, eurPricePerPerson)

        return tentModel
