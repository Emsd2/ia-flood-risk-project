from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold 

def run():
    #Build a list of stations
    stations = build_station_list()
    #update the water levels for each station 
    update_water_levels(stations)
    #find the stations that are over the threshold where tol = 0.8 
    stations_over_threshhold = stations_level_over_threshold(stations, 0.8) 

    for station, waterlevel in stations_over_threshhold:
        print(station.name, waterlevel)
        
if __name__ == "__main__":
    print("*** Task 2B: CUED Part 1A Flood Warning System ***")
    run()
