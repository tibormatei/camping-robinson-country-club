# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_model_builder.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class returns the TrailerModel with dates.
"""

from data import RentalDetailsDataAccess
from data import TrailerModelBuilder
from models.rental_details import TrailerModel
from models.rental_details import TrailersModel


class TrailersModelBuilder():
    """
    This class returns the TrailersModel with dates.
    """

    def __init__(self, data_access: RentalDetailsDataAccess):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailersModelBuilder self parameter.
            data_access: RentalDetailsDataAccess's inheritance class.
        """
        self._data_access = data_access
        self._trailer_model_builder = TrailerModelBuilder(data_access)

    def retrive_trailers_model(self) -> TrailersModel:
        """
        Retrive TrailersModel with dates.

        Args:
            self: TrailersModelBuilder self parameter.
        Returns:
            Returns the TrailersModel with dates.
        """
        trailer_models: list[TrailerModel] = []
        for i in self._data_access.get_trailer_capacities():
            trailer_model: TrailerModel = self._trailer_model_builder.retrive_trailer_model(i)
            trailer_models.append(trailer_model)

        trailers_model: TrailersModel = TrailersModel(trailer_models)

        return trailers_model
