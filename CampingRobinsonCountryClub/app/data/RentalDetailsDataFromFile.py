# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: RentalDetailsDataFromFile.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class reading rental details dates from files.
"""

from pathlib import Path

from app.data import RentalDetailsDataAccess


class RentalDetailsDataFromFile(RentalDetailsDataAccess):
    """
    @summary: This is an abstract base class for Rental details data.
    """

    def __init__(self):
        """
        @summary: The init method initialize instance attributes.
        @param self: RentalDetailsDataFromFile self parameter.
        """
        _TENT_PERSON_FILE_NAME: str = 'tent_person.txt'
        self._TENT_PERSON_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('data', 'txt', _TENT_PERSON_FILE_NAME)

        _TENT_PRICE_FILE_NAME: str = 'tent_price.txt'
        self._TENT_PRICE_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('data', 'txt', _TENT_PRICE_FILE_NAME)

        _TRAILER_FILE_NAME: str = 'trailer.txt'
        self._TRAILER_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('data', 'txt',  _TRAILER_FILE_NAME)

        _DOG_FILE_NAME: str = 'dog.txt'
        self._DOG_FILE_PATH: Path = Path(__file__).parent.parent.parent.joinpath('data', 'txt',  _DOG_FILE_NAME)

    def getTentPersons(self) -> list[str]:
        """
        @summary: Return Tent Persons dates.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns Tent Person dates.
        """
        persons: list[str] = []
        with open(self._TENT_PERSON_FILE_PATH, 'r') as f:
            for line in f:
                person: str = line.removesuffix('\n')
                persons.append(person)

        return persons

    def getTentPriceLei(self) -> int:
        """
        @summary: Return Lei prices from the txt.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns Lei prices from the txt file.
        """
        price: int = -1
        try:
            with open(self._TENT_PRICE_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    currency: str = words[1]
                    if currency.lower() == "lei":
                        price = int(words[0])
        except Exception as e:
            print(f"The getTentPriceLei did not found lei price! Error: {e}")
        finally:
            return price

    def getTentPriceEur(self) -> int:
        """
        @summary: Return Eur prices from the txt.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns Eur prices from the txt file.
        """
        price: int = -1
        try:
            with open(self._TENT_PRICE_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    currency: str = words[1]
                    if currency.lower() == "eur":
                        price = int(words[0])
        except Exception as e:
            print(f"The getTentPriceLei did not found eur price! Error: {e}")
        finally:
            return price

    def getTrailerCapacities(self) -> list[str]:
        """
        @summary: Return capacities of trailer from the txt file.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns capacities of trailer.
        """
        capacities: list[str] = list()
        try:
            with open(self._TRAILER_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    CAPACITY_INDEX = 0
                    capacities.append(words[CAPACITY_INDEX])
        except Exception as e:
            print(f"getTrailerCapacity error: {e}")
        finally:
            return capacities

    def getTrailerPriceLei(self, capacity: str) -> int:
        """
        @summary: Return price of trailer in lei from the txt file.
        @param self: RentalDetailsDataFromFile self parameter.
        @param capacity: Trailer capacity.
        @returns: Returns price of trailer in lei.
        """
        price: int = -1
        try:
            with open(self._TRAILER_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    CAPACITY_INDEX = 0
                    if words[CAPACITY_INDEX] == capacity:
                        LEI_INDEX: int = 2
                        currency: str = words[LEI_INDEX]
                        if currency.lower() == "lei":
                            LEI_PRICE_INDEX: int = 1
                            price = int(words[LEI_PRICE_INDEX])
        except Exception as e:
             print(f"getTrailerPriceLei error: {e}")
        finally:
            return price

    def getTrailerPriceEur(self, capacity: str) -> int:
        """
        @summary: Return price of trailer in eur from the txt file.
        @param self: RentalDetailsDataFromFile self parameter.
        @param capacity: Trailer capacity.
        @returns: Returns price of trailer in eur.
        """
        price: int = -1
        try:
            with open(self._TRAILER_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    CAPACITY_INDEX = 0
                    if words[CAPACITY_INDEX] == capacity:
                        EUR_INDEX: int = 4
                        currency: str = words[EUR_INDEX]
                        if currency.lower() == "eur":
                            EUR_PRICE_INDEX: int = 3
                            price = int(words[EUR_PRICE_INDEX])
        except Exception as e:
             print(f"getTrailerPriceEur error: {e}")
        finally:
            return price

    def getDogPriceLei(self) -> int:
        """
        @summary: Return price of dog in lei from the txt file.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns price of dog in lei.
        """
        price: int = -1
        try:
            with open(self._DOG_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    LEI_INDEX: int = 1
                    currency: str = words[LEI_INDEX]
                    if currency.lower() == "lei":
                        LEI_PRICE_INDEX: int = 0
                        price = int(words[LEI_PRICE_INDEX])
        except Exception as e:
             print(f"getDogPriceLei error: {e}")
        finally:
            return price

    def getDogPriceEur(self) -> int:
        """
        @summary: Return price of dog in eur from the txt file.
        @param self: RentalDetailsDataFromFile self parameter.
        @returns: Returns price of dog in eur.
        """
        price: int = -1
        try:
            with open(self._DOG_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    EUR_INDEX: int = 1
                    currency: str = words[EUR_INDEX]
                    if currency.lower() == "eur":
                        EUR_PRICE_INDEX: int = 0
                        price = int(words[EUR_PRICE_INDEX])
        except Exception as e:
             print(f"getDogPriceEur error: {e}")
        finally:
            return price
