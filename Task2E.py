import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level



def run():

    stations = build_station_list()
    update_water_levels(stations)
    N = 5
    station_list = stations_highest_rel_level(stations, N)

    #Creates a list of the all the station data for the 5 most flooded stations
    greatest_stations = []
    for station1 in station_list:
        for station2 in stations:
            if station2.name == station1[0]:
                greatest_stations.append(station2)


    for station in greatest_stations:

        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()