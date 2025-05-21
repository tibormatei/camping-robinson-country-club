# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TentModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental tent prices.
"""


class TentModel() :
    """
    @summary: This class is a model of rental tent prices.
    """

    def __init__(self) :
        """
        @summary: The init method initialize instance attributes.
        @param self: TestModel self parameter.
        """
        self._tentCapacities = list[str]
        self._leiPricePerPerson = 0
        self._eurPricePerPerson = 0

    @property
    def TentCapacities(self) -> list[str] :
        """
        @summary: The TentCapacities getter property.
        @param self: TestModel self parameter.
        @returns: Returns all tent capacity types.
        """
        return self._tentCapacities

    @property
    def LeiPricePerPerson(self) -> int :
        """
        @summary: The LeiPricePerPerson getter property.
        @param self: TestModel self parameter.
        @returns: Returns price in lei.
        """
        return self._leiPricePerPerson

    @property
    def LeiPricePerPerson(self, leiPricePerPerson : int) :
        """
        @summary: The LeiPricePerPerson setter property.
        @param self: TestModel self parameter.
        @param leiPricePerPerson: Lei price value.
        """
        if leiPricePerPerson > 0 :
            self._leiPricePerPerson = leiPricePerPerson

    @property
    def EurPricePerPerson(self) -> int :
        """
        @summary: The EurPricePerPerson getter property.
        @param self: TestModel self parameter.
        @returns: Returns price in eur.
        """
        return self._eurPricePerPerson

    @property
    def EurPricePerPerson(self, eurPricePerPerson : int) :
        """
        @summary: The EurPricePerPerson setter property.
        @param self: TestModel self parameter.
        @param eurPricePerPerson: Eur price value.
        """
        if eurPricePerPerson > 0 :
            self._eurPricePerPerson = eurPricePerPerson

    @classmethod
    def AddTentCapacity(self, tentcapacity : str) :
        """
        @summary: Add to the list a tent capacity.
        @param self: TestModel self parameter.
        @param tentcapacity: The tent capacity.
        """
        if tentcapacity not in self._tentCapacities :
            self._tentCapacities.append(tentcapacity)
