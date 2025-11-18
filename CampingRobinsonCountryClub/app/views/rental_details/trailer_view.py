# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class handles the view of rental trailer details.
"""


class TrailerView():
    """
    This class handles the view of rental trailer details.
    """

    def __init__(self):
        """
        Rental trailer details views.

        Args:
            self: TrailerView self parameter.
        """
        pass

    @classmethod
    def show_trailer_view(cls, translations: dict, trailer_capacity: str, lei_price: int, eur_price: int) -> str:
        """
        Create a trailer row view.

        Args:
            cls: TrailerView cls parameter.
            translations: Language dictionary.
            trailer_capacity: Capacity data.
            lei_price: Price data in Lei.
            eur_price: Price data in Eur.
        Returns:
            Returns a trailer html table row code piece.
        """
        price_name: str = translations['rentalDetails']['trailerDetails']['personName']

        capacity_data_cell: str = '<td>' + trailer_capacity + ' ' + price_name + '</td>'
        leiDataCell: str = '<td>' + str(lei_price) + '</td>'
        eurDataCell: str = '<td>' + str(eur_price) + '</td>'

        trailer_table_row: str = '<tr>' + capacity_data_cell + leiDataCell + eurDataCell + "</tr>"
        return trailer_table_row

    def __str__(self) -> str:
        """
        A function of a class that can return class state.

        Args:
            self: TrailerView self parameter.
        """
        return self.show_trailer_view()
