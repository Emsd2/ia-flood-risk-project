from floodsystem.geo import stations_by_distance
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_river

from floodsystem.station import MonitoringStation
A = MonitoringStation("s_id1", "m_id1", "station1", (1,1), (0.1,0.1), "riverA", "town1")
B = MonitoringStation("s_id2", "m_id2", "station2", (2,2), (0.2,0.2), "riverA", "town2")
C = MonitoringStation("s_id3", "m_id3", "station3", (3,3), (0.3,0.3), "riverB", "town3")
D = MonitoringStation("s_id4", "m_id4", "station4", (4,4), (0.4,0.4), "riverB", "town4")
E = MonitoringStation("s_id5", "m_id5", "station5", (5,5), (0.5,0.5), "riverC", "town5")

stations = [A, B, C, D, E]

def test_stations_by_distance():
    stations_list = stations_by_distance(stations, (0,0))
    assert type(stations_list) == list
    assert type(stations_list[0]) == tuple
    assert round(stations_list[0][1], 0) == 157

def test_stations_within_radius():
    stations_list = stations_within_radius(stations, (0,0), 400)
    assert type(stations_list) == list
    assert len(stations_list) == 2

def test_rivers_with_station():
    rivers_list = rivers_with_station(stations)
    assert type(rivers_list) == list
    assert len(rivers_list) == 3

def test_stations_by_river():
    rivers_list = stations_by_river(stations)
    assert type(rivers_list) == dict
    assert len(rivers_list) == 3

def test_rivers_by_station_number():
    stations_list = rivers_by_station_number(stations, 1)
    assert type(stations_list) == list
    assert len(stations_list) == 2 
