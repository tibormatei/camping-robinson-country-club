# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental details.
"""

from models.rental_details import TentModel
from models.rental_details import TrailersModel
from models.rental_details import DogModel


class RentalDetailsModel():
    """
    @summary: This class is a model of rental details.
    """

    def __init__(self, tentModel: TentModel = None, trailersModel: TrailersModel = None,
                 dogModel: DogModel = None, priceInformation: str = '', checkOutInformation: str = ''):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsModel self parameter.
        @param tentModel: Tent rental detalis.
        @param trailersModel: Trailer rental detalis.
        @param dogModel: Dog price details.
        @param priceInformation: Price details.
        @param checkOutInformation: Check out time.
        """
        self._tentModel: TentModel = tentModel
        self._trailersModel: TrailersModel = trailersModel
        self._dogModel: DogModel = dogModel
        self._priceInformation: str = priceInformation
        self._checkOutInformation: str = checkOutInformation

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

    @property
    def PriceInformation(self) -> str:
        """
        @summary: The PriceInformation getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns price information detailes.
        """
        return self._priceInformation

    @property
    def CheckOutInformation(self) -> str:
        """
        @summary: The CheckOutInformation getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns check out detailes.
        """
        return self._checkOutInformation
