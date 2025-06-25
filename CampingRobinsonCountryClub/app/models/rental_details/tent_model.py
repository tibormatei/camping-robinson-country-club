# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: tent_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental tent prices.
"""


class TentModel():
    """
    @summary: This class is a model of rental tent prices.
    """

    def __init__(self, tentCapacities: list[str] = [], leiPricePerPerson: int = 0, eurPricePerPerson: int = 0):
        """
        @summary: The init method initialize instance attributes.
        @param self: TestModel self parameter.
        @param tentCapacities: Tent capacities.
        @param leiPricePerPerson: Price in Lei.
        @param eurPricePerPerson: Price in Eur.
        """
        self._tentCapacities: list[str] = tentCapacities
        self._leiPricePerPerson: int = leiPricePerPerson
        self._eurPricePerPerson: int = eurPricePerPerson

    @property
    def TentCapacities(self) -> list[str]:
        """
        @summary: The TentCapacities getter property.
        @param self: TestModel self parameter.
        @returns: Returns all tent capacity types.
        """
        return self._tentCapacities

    @property
    def LeiPricePerPerson(self) -> int:
        """
        @summary: The LeiPricePerPerson getter property.
        @param self: TestModel self parameter.
        @returns: Returns price in lei.
        """
        return self._leiPricePerPerson

    @LeiPricePerPerson.setter
    def LeiPricePerPerson(self, leiPricePerPerson: int):
        """
        @summary: The LeiPricePerPerson setter property.
        @param self: TestModel self parameter.
        @param leiPricePerPerson: Lei price value.
        """
        if leiPricePerPerson > 0:
            self._leiPricePerPerson = leiPricePerPerson

    @property
    def EurPricePerPerson(self) -> int:
        """
        @summary: The EurPricePerPerson getter property.
        @param self: TestModel self parameter.
        @returns: Returns price in eur.
        """
        return self._eurPricePerPerson

    @EurPricePerPerson.setter
    def EurPricePerPerson(self, eurPricePerPerson: int):
        """
        @summary: The EurPricePerPerson setter property.
        @param self: TestModel self parameter.
        @param eurPricePerPerson: Eur price value.
        """
        if eurPricePerPerson > 0:
            self._eurPricePerPerson = eurPricePerPerson

    def AddTentCapacity(self, tentcapacity: str) -> None:
        """
        @summary: Add to the list a tent capacity.
        @param self: TestModel self parameter.
        @param tentcapacity: The tent capacity.
        """
        if tentcapacity not in self._tentCapacities:
            self._tentCapacities.append(tentcapacity)
