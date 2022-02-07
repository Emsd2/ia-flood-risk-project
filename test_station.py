# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

import pytest
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():

    station_1 = MonitoringStation("S1", "Measure S1", "Station1", (10.0, 40.0), None, "Medium River", "Town1")
    station_2 = MonitoringStation("S2", "Measure S1", "Station2", (0.0, 10.0), (1.0, 2.0), "Big River", "Town2")
    station_3 = MonitoringStation("S3", "Measure S3", "Station3", (0.0, 20.0), (2.0, 1.0), "Big River", "Town3")

    station_list = [station_1, station_2, station_3]

    assert type(inconsistent_typical_range_stations(station_list)) == list

    assert len(inconsistent_typical_range_stations(station_list)) == 2

    assert inconsistent_typical_range_stations(station_list)[0] == "Station1"

    assert inconsistent_typical_range_stations(station_list)[1] == "Station3"






    


