# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: DogModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of dog price.
"""


class DogModel():
    """
    @summary: This class is a model of dog price.
    """

    def __init__(self, leiPricePerNight: int = 0, eurPricePerNight: int = 0):
        """
        @summary: The init method initialize instance attributes.
        @param self: DogModel self parameter.
        @param leiPricePerNight: Price in Lei.
        @param eurPricePerNight: Price in Eur.
        """
        self._leiPricePerNight: int = leiPricePerNight
        self._eurPricePerNight: int = eurPricePerNight

    @property
    def LeiPricePerNight(self) -> int:
        """
        @summary: The LeiPricePerNight getter property.
        @param self: DogModel self parameter.
        @returns: Returns price in lei.
        """
        return self._leiPricePerNight

    @LeiPricePerNight.setter
    def LeiPricePerNight(self, leiPricePerNight: int):
        """
        @summary: The LeiPricePerNight setter property.
        @param self: DogModel self parameter.
        @param leiPricePerNight: Lei price value.
        """
        if leiPricePerNight > 0:
            self._leiPricePerNight = leiPricePerNight

    @property
    def EurPricePerNight(self) -> int:
        """
        @summary: The EurPricePerNight getter property.
        @param self: DogModel self parameter.
        @returns: Returns price in eur.
        """
        return self._eurPricePerNight

    @EurPricePerNight.setter
    def EurPricePerNight(self, eurPricePerNight: int):
        """
        @summary: The EurPricePerNight setter property.
        @param self: DogModel self parameter.
        @param eurPricePerNight: Eur price value.
        """
        if eurPricePerNight > 0:
            self._eurPricePerNight = eurPricePerNight
