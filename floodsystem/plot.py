import matplotlib.pyplot as plt
import matplotlib
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    #This plots a graph of time against the levels
    plt.plot(dates, station.typical_range[0], label ="$\typical low level$")
    plt.plot(dates, station.typical_range[1], label ="$\typical high level$")
    plt.plot(dates, levels, label ="$\actual level$")
    #Adds th axis labels and plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels,p):
    plt.plot(dates, station.typical_range[0], label ="$\typical low level$")
    plt.plot(dates, station.typical_range[1], label ="$\typical high level$")
    plt.plot(dates, levels, label ="$\actual level$")

    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    plt.plot(dates, poly(x - d0))

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()
    plt.show()