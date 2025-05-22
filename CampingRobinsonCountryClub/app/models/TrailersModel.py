# Copyright (c) 2025 Matei Tibor. All rights reserved.
#
# Filename: TrailersModel.py
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License.

"""
@summary: This class is a model of rental trailers prices.
"""

from app.models import TrailerModel


class TrailersModel() :
    """
    @summary: This class is a model of rental trailers prices.
    """

    def __init__(self, trailerModels : list[TrailerModel] = []) :
        """
        @summary: The init method initialize instance attributes.
        @param self: TrailersModel self parameter.
        @param trailerModels: Trailer models.
        """
        self._trailers : list[TrailerModel] = trailerModels

    def AddTrailerModel(self, trailerModel : TrailerModel) -> None :
        """
        @summary: Add to the trailers list a trailer model.
        @param self: TrailersModel self parameter.
        @param trailerModel: The trailer model.
        """
        if trailerModel not in self._trailers :
            self._trailers.append(trailerModel)

    def __iter__(self) :
        """
        @summary: This is an iterable class.
        @param self: TrailersModel self parameter.
        """
        return iter(self._trailers)
