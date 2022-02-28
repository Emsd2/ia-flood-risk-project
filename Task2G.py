from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import towns_flooding_risk

import datetime

def run():
    #build list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #find the flooding risk in each town as put in flood.py
    towns_risk = towns_flooding_risk(stations, 10)

    for town, risk in towns_risk:
        print(town + ": " + risk)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
