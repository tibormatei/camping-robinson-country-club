# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class returns the TrailerModel with dates.
"""

from data import RentalDetailsDataAccess
from models.rental_details import TrailerModel


class TrailerModelBuilder():
    """
    @summary: This class returns the TrailerModel with dates.
    """

    def __init__(self, dataAccess: RentalDetailsDataAccess):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailerModelBuilder self parameter.
        @param sedataAccesslf: RentalDetailsDataAccess's inheritance class.
        """
        self._dataAccess = dataAccess

    def RetriveTrailerModel(self, trailerCapacity: str) -> TrailerModel:
        """
        @summary: Retrive TrailerModel with dates.
        @param self: TrailerModelBuilder self parameter.
        @returns: Returns the TrailerModel with dates.
        """
        leiPrice = self._dataAccess.getTrailerPriceLei(trailerCapacity)
        eurPrice = self._dataAccess.getTrailerPriceEur(trailerCapacity)
        trailerModel: TrailerModel = TrailerModel(trailerCapacity, leiPrice, eurPrice)

        return trailerModel
