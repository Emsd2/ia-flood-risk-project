from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    #using 10 different stations
    N=10

    #build a list of 10 stations with the highest relative values
    stations_over_threshold=stations_highest_rel_level(stations, N)

    #print the list
    for station in stations_over_threshold:
        print(station.name, station.relative_water_level())
    
if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")

    run()


