import datetime
from floodsystem.plot import plot_water_level_with_fit
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

        dt = 2
        dates, levels = fetch_measure_levels(station.measure_id,
                                             dt=datetime.timedelta(days=dt))
        p = 4
        if len(dates) == 0 or len(levels) == 0:
            continue
        else:
            plot_water_level_with_fit(station, dates, levels, p)



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()