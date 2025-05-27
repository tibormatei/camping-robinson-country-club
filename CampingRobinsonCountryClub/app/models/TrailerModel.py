# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TrailerModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental trailer prices.
"""


class TrailerModel():
    """
    @summary: This class is a model of rental trailer prices.
    """

    def __init__(self, trailerCapacity: str = '-', leiPrice: int = 0, eurPrice: int = 0):
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailerModel self parameter.
        @param trailerCapacity: Trailer capacity.
        @param leiPrice: Price in Lei.
        @param eurPrice: Price in Eur.
        """
        self._trailerCapacity: str = trailerCapacity
        self._leiPrice: int = leiPrice
        self._eurPrice: int = eurPrice

    @property
    def TrailerCapacity(self) -> str:
        """
        @summary: The TrailerCapacity getter property.
        @param self: TrailerModel self parameter.
        @returns: Returns trailer capacity.
        """
        return self._trailerCapacity

    @TrailerCapacity.setter
    def TrailerCapacity(self, trailerCapacity: str):
        """
        @summary: The TrailerCapacity setter property.
        @param self: TrailerModel self parameter.
        @param trailerCapacity: Trailer capacity.
        """
        if trailerCapacity != "":
            self._trailerCapacity = trailerCapacity

    @property
    def LeiPrice(self) -> int:
        """
        @summary: The LeiPrice getter property.
        @param self: TrailerModel self parameter.
        @returns: Returns price in Lei.
        """
        return self._leiPrice

    @LeiPrice.setter
    def LeiPrice(self, leiPrice: int):
        """
        @summary: The LeiPrice setter property.
        @param self: TrailerModel self parameter.
        @param leiPrice: Price in Lei.
        """
        if leiPrice > 0:
            self._leiPrice = leiPrice

    @property
    def EurPrice(self) -> int:
        """
        @summary: The EurPrice getter property.
        @param self: TrailerModel self parameter.
        @returns: Returns price in Eur.
        """
        return self._eurPrice

    @EurPrice.setter
    def EurPrice(self, eurPrice: int):
        """
        @summary: The EurPrice setter property.
        @param self: TrailerModel self parameter.
        @param eurPrice: Price in Eur.
        """
        if eurPrice > 0:
            self._eurPrice = eurPrice
