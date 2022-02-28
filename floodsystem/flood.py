from .utils import sorted_by_key
from .station import MonitoringStation

#define the stations with their water level being over the threshold of 0.8 
def stations_level_over_threshold(stations, tol):
    #create an empty list of tuples
    tuples = []
    #loop through each station
    for station in stations:
        waterlevel = station.relative_water_level()
        if waterlevel is not None and waterlevel > tol:
            # Add tuple to list
            tuples.append((station, waterlevel))

    # Sort list
    return sorted_by_key(tuples, 1, True)

def stations_highest_rel_level(stations, N):
    #create list of stations with their relative level
    stations_level = []
    for station in stations:
        waterlevel = station.relative_water_level()
        if waterlevel is not None:
            stations_level.append((station, waterlevel))
    #sort the list of stations in descending order of water level
    stations_level = sorted_by_key(stations_level, 1, True)
    #return first N
    return [x[0] for x in stations_level[:N]]

def towns_average_level(stations):
    """ Returns towns with the average relative water level """
    towns_stations = {}

    for station in stations:
        #add the station to the dictionary town stations
        try:
            towns_stations[station.town].append(station)
        except:
            towns_stations[station.town] = [station]
        
    towns_average_level = []
    for town, stations in towns_stations.items():
        #find the mean water level of all the stations in the town
        mean_level = 0
        number = 0
        for station in stations:
            if not station.relative_water_level() == None:
                mean_level += station.relative_water_level()
                number += 1
        if number > 0:
            mean_level /= number
            towns_average_level.append((town, mean_level))

    #sort list of towns by their water level
    towns_average_level = sorted_by_key(towns_average_level, 1, True)

    return towns_average_level

def towns_flooding_risk(stations, N):
    """ Return list of towns and risk of flooding """
    #find the flooding level of each town
    towns_level = towns_average_level(stations)[:N]
    towns_risk = []
    #give a rating of each water level in town
    for town, level in towns_level:
        risk = "Low"
        if level > 2:
            risk = "Severe"
        elif level > 1.5:
            risk = "High"
        elif level > 1:
            risk = "Moderate"
        towns_risk.append((town, risk))
    return towns_risk

