# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental details.
"""

from app.models import TentModel
from app.models import TrailersModel
from app.models import DogModel


class RentalDetailsModel():
    """
    @summary: This class is a model of rental details.
    """

    def __init__(self, tentModel: TentModel = None, trailersModel: TrailersModel = None, dogModel: DogModel = None):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsModel self parameter.
        @param tentModel: Tent rental detalis.
        @param trailersModel: Trailer rental detalis.
        @param dogModel: Dog price details.
        """
        self._tentModel: TentModel = tentModel
        self._trailersModel: TrailersModel = trailersModel
        self._dogModel: DogModel = dogModel

    @property
    def TentModel(self) -> TentModel:
        """
        @summary: The TentModel getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns tent detailes.
        """
        return self._tentModel

    @property
    def TrailersModel(self) -> TrailersModel:
        """
        @summary: The TrailersModel getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns trailers detailes.
        """
        return self._trailersModel
    
    @property
    def DogModel(self) -> DogModel:
        """
        @summary: The DogModel getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns dog detailes.
        """
        return self._dogModel
