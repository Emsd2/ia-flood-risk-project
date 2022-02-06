
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():

    stations_distance_list = []
    stations = build_station_list()
    stations_distance_list = stations_by_distance(stations, (52.2053,0.1218))
    #Created a dictionary which relates the station name to the location of the station
    location = {}
    for station in stations:
        location.update({station.name : station.town})

    closest = stations_distance_list[:10]
    furthest = stations_distance_list[-10:]
    closest_list = []
    furthest_list = []
    
    #For loop loops through the station information for the 10 closest stations
    for station in closest:
        #Finds the corresponding town for the station and adds the station name, town and distance to a list
        town = location[station[0]]
        temp = (station[0], town, station[1])
        closest_list.append(temp)
        
    #For loop loops through the station information for the 10 furthest stations
    for station in furthest:
        #Finds the corresponding town for the station and adds the station name, town and distance to a list
        town = location[station[0]]
        temp = (station[0], town, station[1])
        furthest_list.append(temp)

    print(closest_list)
    print(furthest_list)

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()