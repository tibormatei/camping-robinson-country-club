# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model of rental trailer prices.
"""


class TrailerModel():
    """
    This class is a model of rental trailer prices.
    """

    def __init__(self, trailer_capacity: str = '-', lei_price: int = 0, eur_price: int = 0):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailerModel self parameter.
            trailer_capacity: Trailer capacity.
            lei_price: Price in Lei.
            eur_price: Price in Eur.
        """
        self._trailer_capacity: str = trailer_capacity
        self._lei_price: int = lei_price
        self._eur_price: int = eur_price

    @property
    def trailer_capacity(self) -> str:
        """
        The trailer_capacity getter property.

        Args:
            self: TrailerModel self parameter.
        Returns:
            Returns trailer capacity.
        """
        return self._trailer_capacity

    @trailer_capacity.setter
    def trailer_capacity(self, trailer_capacity: str):
        """
        The trailer_capacity setter property.

        Args:
            self: TrailerModel self parameter.
            trailer_capacity: Trailer capacity.
        """
        if trailer_capacity != "":
            self._trailer_capacity = trailer_capacity

    @property
    def lei_price(self) -> int:
        """
        The lei_price getter property.

        Args:
            self: TrailerModel self parameter.
        Returns:
            Returns price in Lei.
        """
        return self._lei_price

    @lei_price.setter
    def lei_price(self, lei_price: int):
        """
        The lei_price setter property.

        Args:
            self: TrailerModel self parameter.
            lei_price: Price in Lei.
        """
        if lei_price > 0:
            self._lei_price = lei_price

    @property
    def eur_price(self) -> int:
        """
        The eur_price getter property.

        Args:
            self: TrailerModel self parameter.
        Returns:
            Returns price in Eur.
        """
        return self._eur_price

    @eur_price.setter
    def eur_price(self, eur_price: int):
        """
        The eur_price setter property.

        Args:
            self: TrailerModel self parameter.
            eur_price: Price in Eur.
        """
        if eur_price > 0:
            self._eur_price = eur_price
