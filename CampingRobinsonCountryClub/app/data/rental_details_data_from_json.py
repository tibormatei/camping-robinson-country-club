# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_data_from_json.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class reading rental details dates from json files.
"""

from pathlib import Path
import json

from data import RentalDetailsDataAccess


class RentalDetailsDataFromJson(RentalDetailsDataAccess):
    """
    @summary: This is an abstract base class for Rental details data.
    """

    LEI_KEY = 'lei'
    EUR_KEY = 'eur'

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsDataFromJson self parameter.
        """
        # 1.
        TENT_FILE_NAME: str = 'tent.json'
        TENT_FILE_PATH: Path = Path(__file__).parent.joinpath('json', TENT_FILE_NAME)
        try:
            f = open(file = TENT_FILE_PATH, mode = 'r', encoding = 'utf-8')
            self._TENT = json.load(f)
            f.close()

        except FileNotFoundError:
            print(f'Json file not found: {TENT_FILE_PATH}!')
            self._TENT = {}

        # 2.
        TRAILER_FILE_NAME: str = 'trailer.json'
        TRAILER_FILE_PATH: Path = Path(__file__).parent.joinpath('json', TRAILER_FILE_NAME)
        try:
            f = open(file = TRAILER_FILE_PATH, mode = 'r', encoding = 'utf-8')
            self._TRAILER = json.load(f)
            f.close()

        except FileNotFoundError:
            print(f'Json file not found: {TRAILER_FILE_PATH}!')
            self._TRAILER = {}

        # 3.
        DOG_FILE_NAME: str = 'dog.json'
        DOG_FILE_PATH: Path = Path(__file__).parent.joinpath('json', DOG_FILE_NAME)
        try:
            f = open(file = DOG_FILE_PATH, mode = 'r', encoding = 'utf-8')
            self._DOG = json.load(f)
            f.close()

        except FileNotFoundError:
            print(f'Json file not found: {DOG_FILE_PATH}!')
            self._DOG = {}

    def getTentPersons(self) -> list[str]:
        """
        @summary: Return Tent Persons dates.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns Tent Person dates.
        """
        persons: list[str] = []
        if len(self._TENT) > 0:
            TENT_PERSONS_KEY = 'tentPersons'
            for person in self._TENT[TENT_PERSONS_KEY]:
                persons.append(person)

        return persons

    def getTentPriceLei(self) -> int:
        """
        @summary: Return Lei prices from the json.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns Lei prices from the json file.
        """
        price: int = -1
        if len(self._TENT) > 0:
            price = self._TENT[self.LEI_KEY]

        return price

    def getTentPriceEur(self) -> int:
        """
        @summary: Return Eur prices from the json.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns Eur prices from the json file.
        """
        price: int = -1
        if len(self._TENT) > 0:
            price = self._TENT[self.EUR_KEY]

        return price

    def getTrailerCapacities(self) -> list[str]:
        """
        @summary: Return capacities of trailer from the json file.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns capacities of trailer.
        """
        capacities: list[str] = list()
        if len(self._TRAILER) > 0:
            TRAILER_CAPACITIES_KEY = 'trailerCapacities'
            for person in self._TRAILER[TRAILER_CAPACITIES_KEY]:
                capacities.append(person)

        return capacities

    def getTrailerPriceLei(self, capacity: str) -> int:
        """
        @summary: Return price of trailer in lei from the json file.
        @param self: RentalDetailsDataFromJson self parameter.
        @param capacity: Trailer capacity.
        @returns: Returns price of trailer in lei.
        """
        price: int = -1
        if len(self._TRAILER) > 0:
            price = self._TRAILER[capacity][self.LEI_KEY]

        return price

    def getTrailerPriceEur(self, capacity: str) -> int:
        """
        @summary: Return price of trailer in eur from the json file.
        @param self: RentalDetailsDataFromJson self parameter.
        @param capacity: Trailer capacity.
        @returns: Returns price of trailer in eur.
        """
        price: int = -1
        if len(self._TRAILER) > 0:
            price = self._TRAILER[capacity][self.EUR_KEY]

        return price

    def getDogPriceLei(self) -> int:
        """
        @summary: Return price of dog in lei from the json file.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns price of dog in lei.
        """
        price: int = -1
        if len(self._DOG) > 0:
            price = self._DOG[self.LEI_KEY]

        return price

    def getDogPriceEur(self) -> int:
        """
        @summary: Return price of dog in eur from the json file.
        @param self: RentalDetailsDataFromJson self parameter.
        @returns: Returns price of dog in eur.
        """
        price: int = -1
        if len(self._DOG) > 0:
            price = self._DOG[self.EUR_KEY]

        return price
