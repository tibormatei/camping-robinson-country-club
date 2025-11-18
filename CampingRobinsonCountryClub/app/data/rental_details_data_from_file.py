# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: rental_details_data_from_file.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class reading rental details dates from files.
"""

from pathlib import Path

from data import RentalDetailsDataAccess


class RentalDetailsDataFromFile(RentalDetailsDataAccess):
    """
    This is an abstract base class for Rental details data.
    """

    def __init__(self):
        """
        The init method initialize instance attributes.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        """
        TENT_PERSON_FILE_NAME: str = 'tent_person.txt'
        self._TENT_PERSON_FILE_PATH: Path = Path(__file__).parent.joinpath('txt', TENT_PERSON_FILE_NAME)

        TENT_PRICE_FILE_NAME: str = 'tent_price.txt'
        self._TENT_PRICE_FILE_PATH: Path = Path(__file__).parent.joinpath('txt', TENT_PRICE_FILE_NAME)

        TRAILER_FILE_NAME: str = 'trailer.txt'
        self._TRAILER_FILE_PATH: Path = Path(__file__).parent.joinpath('txt', TRAILER_FILE_NAME)

        DOG_FILE_NAME: str = 'dog.txt'
        self._DOG_FILE_PATH: Path = Path(__file__).parent.joinpath('txt', DOG_FILE_NAME)

    def get_tent_persons(self) -> list[str]:
        """
        Return Tent Persons dates.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns Tent Person dates.
        """
        persons: list[str] = []
        with open(self._TENT_PERSON_FILE_PATH, 'r') as f:
            for line in f:
                person: str = line.removesuffix('\n')
                persons.append(person)

        return persons

    def get_tent_price_lei(self) -> int:
        """
        Return Lei prices from the txt.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns Lei prices from the txt file.
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
            print(f"The get_tent_price_lei did not found lei price! Error: {e}")
        finally:
            return price

    def get_tent_price_eur(self) -> int:
        """
        Return Eur prices from the txt.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns Eur prices from the txt file.
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
            print(f"The get_tent_price_eur did not found eur price! Error: {e}")
        finally:
            return price

    def get_trailer_capacities(self) -> list[str]:
        """
        Return capacities of trailer from the txt file.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns capacities of trailer.
        """
        capacities: list[str] = list()
        try:
            with open(self._TRAILER_FILE_PATH) as f:
                for line in f:
                    words: list[str] = line.split()
                    CAPACITY_INDEX = 0
                    capacities.append(words[CAPACITY_INDEX])
        except Exception as e:
            print(f"get_trailer_capacities error: {e}")
        finally:
            return capacities

    def get_trailer_price_lei(self, capacity: str) -> int:
        """
        Return price of trailer in lei from the txt file.

        Args:
            self: RentalDetailsDataFromFile self parameter.
            capacity: Trailer capacity.
        Returns:
            Returns price of trailer in lei.
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
             print(f"get_trailer_price_lei error: {e}")
        finally:
            return price

    def get_trailer_price_eur(self, capacity: str) -> int:
        """
        Return price of trailer in eur from the txt file.

        Args:
            self: RentalDetailsDataFromFile self parameter.
            capacity: Trailer capacity.
        Returns:
            Returns price of trailer in eur.
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
             print(f"get_trailer_price_eur error: {e}")
        finally:
            return price

    def get_dog_price_lei(self) -> int:
        """
        Return price of dog in lei from the txt file.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns price of dog in lei.
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
             print(f"get_dog_price_lei error: {e}")
        finally:
            return price

    def get_dog_price_eur(self) -> int:
        """
        Return price of dog in eur from the txt file.

        Args:
            self: RentalDetailsDataFromFile self parameter.
        Returns:
            Returns price of dog in eur.
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
             print(f"get_dog_price_eur error: {e}")
        finally:
            return price
