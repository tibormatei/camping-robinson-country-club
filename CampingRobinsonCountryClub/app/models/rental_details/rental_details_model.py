# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model of rental details.
"""

from models.rental_details import TentModel
from models.rental_details import TrailersModel
from models.rental_details import DogModel


class RentalDetailsModel():
    """
    This class is a model of rental details.
    """

    def __init__(self, tent_model: TentModel = None, trailers_model: TrailersModel = None,
                 dog_model: DogModel = None, price_information: str = '', check_out_information: str = ''):
        """
        The init method initialize instance attributes.

        Args:
            self: RentalDetailsModel self parameter.
            tent_model: Tent rental detalis.
            trailers_model: Trailer rental detalis.
            dog_model: Dog price details.
            price_information: Price details.
            check_out_information: Check out time.
        """
        self._tent_model: TentModel = tent_model
        self._trailers_model: TrailersModel = trailers_model
        self._dog_model: DogModel = dog_model
        self._price_information: str = price_information
        self._check_out_information: str = check_out_information

    @property
    def tent_model(self) -> TentModel:
        """
        The tent_model getter property.

        Args:
            self: RentalDetailsModel self parameter.
        Returns:
            Returns tent detailes.
        """
        return self._tent_model

    @property
    def trailers_model(self) -> TrailersModel:
        """
        The trailers_model getter property.

        Args:
            self: RentalDetailsModel self parameter.
        Returns:
            Returns trailers detailes.
        """
        return self._trailers_model

    @property
    def dog_model(self) -> DogModel:
        """
        The dog_model getter property.

        Args:
            self: RentalDetailsModel self parameter.
        Returns:
            Returns dog detailes.
        """
        return self._dog_model

    @property
    def price_information(self) -> str:
        """
        The price_information getter property.

        Args:
            self: RentalDetailsModel self parameter.
        Returns:
            Returns price information detailes.
        """
        return self._price_information

    @property
    def check_out_information(self) -> str:
        """
        The CheckOutInformation getter property.

        Args:
            self: RentalDetailsModel self parameter.
        Returns:
            Returns check out detailes.
        """
        return self._check_out_information
