# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class returns the TentModel with dates.
"""

from data import RentalDetailsDataAccess
from models import DogModel


class DogModelBuilder():
    """
    @summary: This class returns the DogModel with dates.
    """

    def __init__(self, dataAccess: RentalDetailsDataAccess):
        """
        @summary: The init method initialize instance attributes.
        @param self: DogModelBuilder self parameter.
        @param sedataAccesslf: RentalDetailsDataAccess's inheritance class.
        """
        self._dataAccess = dataAccess

    def RetriveDogModel(self) -> DogModel:
        """
        @summary: Retrive DogModel with dates.
        @param self: DogModelBuilder self parameter.
        @returns: Returns the DogModel with dates.
        """
        leiPricePerNight: int = self._dataAccess.getDogPriceLei()
        eurPricePerNight: int = self._dataAccess.getDogPriceEur()
        dogModel: DogModel = DogModel(leiPricePerNight, eurPricePerNight)

        return dogModel
