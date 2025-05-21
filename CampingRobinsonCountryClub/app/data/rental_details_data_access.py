# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_data_access.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This is an interface/abstract base class.
"""

from abc import abstractmethod


class RentalDetailsDataAccess():
    """
    @summary: This is an abstract base class for Rental details data.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getTentPersons(self) -> list[str]:
        pass

    @abstractmethod
    def getTentPriceLei(self) -> int:
        pass

    @abstractmethod
    def getTentPriceEur(self) -> int:
        pass

    @abstractmethod
    def getTrailerCapacities(self) -> list[str]:
        pass

    @abstractmethod
    def getTrailerPriceLei(self, capacity: str) -> str:
        pass

    @abstractmethod
    def getTrailerPriceEur(self, capacity: str) -> str:
        pass

    @abstractmethod
    def getDogPriceLei(self) -> int:
        pass

    @abstractmethod
    def getDogPriceEur(self) -> int:
        pass
