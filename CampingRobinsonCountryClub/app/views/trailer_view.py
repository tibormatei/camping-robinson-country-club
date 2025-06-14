# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailer_view.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class handles the view of rental trailer details.
"""


class TrailerView():
    """
    @summary: This class handles the view of rental trailer details.
    """

    def __init__(self):
        """
        @summary: Rental trailer details views.
        @param self: TrailerView self parameter.
        """
        pass

    @classmethod
    def showTrailerView(cls, translations: dict, trailerCapacity: str, leiPrice: int, eurPrice: int) -> str:
        """
        @summary: Create a trailer row view.
        @param cls: TrailerView cls parameter.
        @param translations: Language dictionary.
        @param trailerCapacity: Capacity data.
        @param leiPrice: Price data in Lei.
        @param eurPrice: Price data in Eur.
        @returns: Returns a trailer html table row code piece.
        """
        priceName: str = translations['rentalDetails']['trailerDetails']['personName']

        capacityDataCell: str = '<td>' + trailerCapacity + ' ' + priceName + '</td>'
        leiDataCell: str = '<td>' + str(leiPrice) + '</td>'
        eurDataCell: str = '<td>' + str(eurPrice) + '</td>'

        trailerTableRow: str = '<tr>' + capacityDataCell + leiDataCell + eurDataCell + "</tr>"
        return trailerTableRow

    def __str__(self) -> str:
        """
        @summary: A function of a class that can return class state.
        @param self: TrailerView self parameter.
        """
        return self.showTrailerView()
