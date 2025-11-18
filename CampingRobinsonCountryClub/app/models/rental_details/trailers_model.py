# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: trailers_model.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
This class is a model of rental trailers prices.
"""

from models.rental_details import TrailerModel


class TrailersModel():
    """
    This class is a model of rental trailers prices.
    """

    def __init__(self, trailer_models: list[TrailerModel] = []):
        """
        The init method initialize instance attributes.

        Args:
            self: TrailersModel self parameter.
            trailer_models: Trailer models.
        """
        self._trailers: list[TrailerModel] = trailer_models

    def add_trailer_model(self, trailer_model: TrailerModel) -> None:
        """
        Add to the trailers list a trailer model.

        Args:
            self: TrailersModel self parameter.
            trailer_model: The trailer model.
        """
        if trailer_model not in self._trailers:
            self._trailers.append(trailer_model)

    def __iter__(self):
        """
        This is an iterable class.

        Args:
            self: TrailersModel self parameter.
        """
        return iter(self._trailers)
