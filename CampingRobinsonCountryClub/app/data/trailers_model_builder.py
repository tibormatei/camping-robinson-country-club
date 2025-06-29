# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class returns the TrailerModel with dates.
"""

from data import RentalDetailsDataAccess
from data import TrailerModelBuilder
from models.rental_details import TrailerModel
from models.rental_details import TrailersModel


class TrailersModelBuilder():
    """
    @summary: This class returns the TrailersModel with dates.
    """

    def __init__(self, dataAccess: RentalDetailsDataAccess):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailersModelBuilder self parameter.
        @param sedataAccesslf: RentalDetailsDataAccess's inheritance class.
        """
        self._dataAccess = dataAccess
        self._trailerModelBuilder = TrailerModelBuilder(dataAccess)

    def RetriveTrailersModel(self) -> TrailersModel:
        """
        @summary: Retrive TrailersModel with dates.
        @param self: TrailersModelBuilder self parameter.
        @returns: Returns the TrailersModel with dates.
        """
        trailerModels: list[TrailerModel] = []
        for i in self._dataAccess.getTrailerCapacities():
            trailerModel: TrailerModel = self._trailerModelBuilder.RetriveTrailerModel(i)
            trailerModels.append(trailerModel)

        trailersModel: TrailersModel = TrailersModel(trailerModels)

        return trailersModel
