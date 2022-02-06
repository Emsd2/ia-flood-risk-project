from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    N = 9
    station_number = rivers_by_station_number(stations, N)

    print(station_number)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()