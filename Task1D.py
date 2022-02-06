
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    number_of_rivers = len(rivers)
    rivers.sort()
    print(number_of_rivers , " stations. First 10 - " , rivers[:10])

    rivers_and_stations = stations_by_river(stations)

    print(rivers_and_stations["River Aire"])
    print(rivers_and_stations["River Cam"])
    print(rivers_and_stations["River Thames"])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()