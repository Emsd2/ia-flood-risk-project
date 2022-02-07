from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():

    #list of stations
    stations = build_station_list()
    #finding the stations that are within required radius of 10km of the Cambridge City centre
    stations_required = stations_within_radius(stations, (52.2053, 0.1218), 10)
    #sorting the stations in alphabetical order
    station_list = []
    for station in stations_required:
        #using a list to be able to sort the stations
        station_list.append(station)
    print(sorted(station_list))
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

    
