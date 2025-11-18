# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_data_access.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This is an interface/abstract base class.
"""

from abc import abstractmethod


class RentalDetailsDataAccess():
    """
    This is an abstract base class for Rental details data.
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tent_persons(self) -> list[str]:
        pass

    @abstractmethod
    def get_tent_price_lei(self) -> int:
        pass

    @abstractmethod
    def get_tent_price_eur(self) -> int:
        pass

    @abstractmethod
    def get_trailer_capacities(self) -> list[str]:
        pass

    @abstractmethod
    def get_trailer_price_lei(self, capacity: str) -> str:
        pass

    @abstractmethod
    def get_trailer_price_eur(self, capacity: str) -> str:
        pass

    @abstractmethod
    def get_dog_price_lei(self) -> int:
        pass

    @abstractmethod
    def get_dog_price_eur(self) -> int:
        pass
