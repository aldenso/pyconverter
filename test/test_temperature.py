from nose.tools import *
from pyconverter import temperature


def test_celsius():
    x = temperature.Celsius(40)
    assert_equal(x.getFahrenheit(), 104.0)
    assert_equal(x.units, "Celsius")

def test_fahreheint():
    x = temperature.Fahrenheit(104.0)
    assert_equal(x.getCelsius(), 40.0)
    assert_equal(x.units, "Fahrenheit") 

def test_kelvin():
    x = temperature.Kelvin(313.15)
    assert_equal(x.getCelsius(), 40.0)
    assert_equal(x.getFahrenheit(), 104.0)