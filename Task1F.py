from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent = sorted(inconsistent)
    print(inconsistent)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
