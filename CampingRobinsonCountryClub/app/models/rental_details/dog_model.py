# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: dog_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model of dog price.
"""


class DogModel():
    """
    This class is a model of dog price.
    """

    def __init__(self, lei_price_per_night: int = 0, eur_price_per_night: int = 0):
        """
        The init method initialize instance attributes.

        Args:
            self: DogModel self parameter.
            lei_price_per_night: Price in Lei.
            eur_price_per_night: Price in Eur.
        """
        self._lei_price_per_night: int = lei_price_per_night
        self._eur_price_per_night: int = eur_price_per_night

    @property
    def lei_price_per_night(self) -> int:
        """
        The LeiPricePerNight getter property.

        Args:
            self: DogModel self parameter.
        Returns:
            Returns price in lei.
        """
        return self._lei_price_per_night

    @lei_price_per_night.setter
    def lei_price_per_night(self, lei_price_per_night: int):
        """
        The lei_price_per_night setter property.

        Args:
            self: DogModel self parameter.
            lei_price_per_night: Lei price value.
        """
        if lei_price_per_night > 0:
            self._lei_price_per_night = lei_price_per_night

    @property
    def eur_price_per_night(self) -> int:
        """
        The eur_price_per_night getter property.

        Args:
            self: DogModel self parameter.
        Returns:
            Returns price in eur.
        """
        return self._eur_price_per_night

    @eur_price_per_night.setter
    def eur_price_per_night(self, eur_price_per_night: int):
        """
        The eur_price_per_night setter property.

        Args:
            self: DogModel self parameter.
            eur_price_per_night: Eur price value.
        """
        if eur_price_per_night > 0:
            self._eur_price_per_night = eur_price_per_night
