# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def stations_within_radius(stations, centre, r):
    stationslist = stations_by_distance(stations, centre)
    counter = 0 
    while stationslist[:counter][1] < r: 
        stations.append(stationslist[counter][0])
    return stations



