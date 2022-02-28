#2B testing
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels


#make a test function
def test_stations_level_over_threshold():
    #build a list of stations 
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    tol = 0.8
    y = stations_level_over_threshold(stations, tol)
    for i in stations:
        for z in y:
            if z[0] == i.name:
                assert z[1] == i.relative_water_level(i.latest_level)
                assert z[1] > 0.8

    return

#2C testing
def test_stations_highest_rel_level():
#build a list of stations 
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #make a test function
    N=10
    y = stations_highest_rel_level(stations, N)
    assert len(y) == 10 
    #assure that 10 stations are tested 
    station_names = []
    for each in y:
        station_names.append(each[1])
    for station in stations:
        if station.name in station_names:
            assert y[1] == station.relative_water_level()

