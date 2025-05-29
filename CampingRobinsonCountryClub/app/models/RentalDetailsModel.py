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

from collections.abc import Iterator

from app.controllers import TentController
from app.controllers import TrailersController
from app.controllers import TrailerController
from app.controllers import DogController


class RentalDetailsModel():
    """
    @summary: This class is a model of rental details.
    """

    def __init__(self, tentController: TentController = None, trailersController: TrailersController = None,
                 trailerControllersList: list[TrailerController] = [], dogController: DogController = None,
                 priceInformation: str = '', checkOutinformation: str = ''):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsModel self parameter.
        @param tentController: Tent rental detalis.
        @param trailersController: Trailer rental detalis.
        @param trailerControllersList: Trailer controllers in a list..
        @param dogController: Dog price details.
        @param priceInformation: Price details.
        @param checkOutinformation: Check out time.
        """
        self._tentController: TentController = tentController
        self._trailersController: TrailersController = trailersController
        self._trailerControllersList: list[TrailerController] = trailerControllersList
        self._dogController: DogController = dogController
        self._priceInformation: str = priceInformation
        self._checkOutinformation: str = checkOutinformation

    @property
    def TentController(self) -> TentController:
        """
        @summary: The TentController getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns tent detailes.
        """
        return self._tentModel

    @property
    def TrailersController(self) -> TrailersController:
        """
        @summary: The TrailersController getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns trailers detailes.
        """
        return self._trailersController

    @property
    def TrailerControllersList(self) -> Iterator:
        """
        @summary: The TrailerControllersList getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns trailer controllers.
        """
        return iter(self._trailerControllersList)

    @property
    def DogController(self) -> DogController:
        """
        @summary: The DogController getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns dog detailes.
        """
        return self._dogController

    @property
    def PriceInformation(self) -> str:
        """
        @summary: The PriceInformation getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns price information detailes.
        """
        return self._priceInformation

    @property
    def CheckOutinformation(self) -> str:
        """
        @summary: The CheckOutinformation getter property.
        @param self: RentalDetailsModel self parameter.
        @returns: Returns check out detailes.
        """
        return self._checkOutinformation
