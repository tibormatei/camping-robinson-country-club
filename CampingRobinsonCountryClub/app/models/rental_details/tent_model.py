# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model of rental tent prices.
"""


class TentModel():
    """
    This class is a model of rental tent prices.
    """

    def __init__(self, tent_capacities: list[str] = [], lei_price_per_person: int = 0, eur_price_per_person: int = 0):
        """
        The init method initialize instance attributes.

        Args:
            self: TestModel self parameter.
            tent_capacities: Tent capacities.
            lei_price_per_person: Price in Lei.
            eur_price_per_person: Price in Eur.
        """
        self._tent_capacities: list[str] = tent_capacities
        self._lei_price_per_person: int = lei_price_per_person
        self._eur_price_per_person: int = eur_price_per_person

    @property
    def tent_capacities(self) -> list[str]:
        """
        The tent_capacities getter property.

        Args:
            self: TestModel self parameter.
        Returns:
            Returns all tent capacity types.
        """
        return self._tent_capacities

    @property
    def lei_price_per_person(self) -> int:
        """
        The lei_price_per_person getter property.

        Args:
            self: TestModel self parameter.
        Returns:
            Returns price in lei.
        """
        return self._lei_price_per_person

    @lei_price_per_person.setter
    def lei_price_per_person(self, lei_price_per_person: int):
        """
        The lei_price_per_person setter property.

        Args:
            self: TestModel self parameter.
            lei_price_per_person: Lei price value.
        """
        if lei_price_per_person > 0:
            self._lei_price_per_person = lei_price_per_person

    @property
    def eur_price_per_person(self) -> int:
        """
        The eur_price_per_person getter property.

        Args:
            self: TestModel self parameter.
        Returns:
            Returns price in eur.
        """
        return self._eur_price_per_person

    @eur_price_per_person.setter
    def eur_price_per_person(self, eur_price_per_person: int):
        """
        The eur_price_per_person setter property.

        Args:
            self: TestModel self parameter.
            eur_price_per_person: Eur price value.
        """
        if eur_price_per_person > 0:
            self._eur_price_per_person = eur_price_per_person

    def add_tent_capacity(self, tent_capacity: str) -> None:
        """
        Add to the list a tent capacity.

        Args:
            self: TestModel self parameter.
            tent_capacity: The tent capacity.
        """
        if tent_capacity not in self._tent_capacities:
            self._tent_capacities.append(tent_capacity)
