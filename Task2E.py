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

    
    for station in station_list:

        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        if len(dates) == 0 or len(levels) == 0:
            print("There is no data in the past 10 days for" , station.name)
            continue
        else:
            plot_water_levels(station, dates, levels)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()