# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def stations_within_radius(stations, centre, r):
    stationslist = stations_by_distance(stations, centre)

    stations = []
    for station in stationslist:
        if station[1] <= r:
            stations.append(station[0])

    return stations


from haversine import haversine

def stations_by_distance(stations, p):

    stations_list = []
    #For loop loops through the different stations
    for station in stations:
        #The distance between the p coordinate and the station coordinate is calculated using haversine
        distance = haversine(p, station.coord)
        #Creates a tuple and adds it to the list
        temp = (station.name, distance)
        stations_list.append(temp)

    #sorted_by_key(stations_list, 1)
    stations_list.sort(key = lambda a:a[1])
    return  stations_list



def rivers_with_station(stations):
    rivers = []
    for station in stations:
            rivers.append(station.river)

    actual_river = []
    #For loop loops through the different rivers
    for river in rivers:
        #If the river is not in the river list then it is added
        if river not in actual_river:
            actual_river.append(river)
    
    return actual_river

def stations_by_river(stations):
    
    river_station = {}
    #For loop loops through the different stations
    for station in stations:
        #If the river of the station is in river station then just the station name is added if not then both the station and cooresponding river are added
        if station.river in river_station:    
            river_station[station.river].append(station.name)
            river_station[station.river].sort()
        else:
            river_station.update({station.river: [station.name]})
    
    return river_station

def rivers_by_station_number(stations, N):

    rivers = rivers_with_station(stations)
    stations_river = stations_by_river(stations)

    number_list = []
    #For loop loops through the different rivers
    for river in rivers:
        #calculate the number of stations per river and add the river and number of stations to a list
        number_of_stations = len(stations_river[river])
        number_list.append((river, number_of_stations))
    #To sort a list of tuples by the second element of the tuple and so that the list is in descending order
    #sorted_by_key(number_list, 1, reverse = True)
    number_list.sort(key = lambda a:a[1], reverse = True)

    counter = 0
    number_stations_list = []
    while counter < N :
        number_stations_list.append(number_list[counter])
        counter = counter +1

    for station in number_list:
        if station[1] == number_list[counter-1][1]:
            number_stations_list.append(station)

    return number_stations_list

    
    

        

