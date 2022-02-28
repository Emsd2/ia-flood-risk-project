import numpy as np
import matplotlib.dates as m_dates


def polyfit(dates, levels, p):
    dates_float = []

    for date in dates:
        dates_float.append(m_dates.date2num(date))
   
    p_coeff = np.polyfit(dates_float - dates_float[0], levels, p)
    poly = np.poly1d(p_coeff)

    return (poly , dates_float[0])
