from floodsystem.analysis import polyfit
import numpy

dates = [20,21,22,23,24,25]
levels = [2,2,2,3,3,4]

def test_polyfit():
    poly, d0 = polyfit(dates, levels, 3)
    assert isinstance(poly, numpy.poly1d)
    assert isinstance(d0, float)
    assert d0 > 0
