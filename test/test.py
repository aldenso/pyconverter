from nose.tools import *
from pyconverter import temperature, length

def setup():
    print("SETUP")

def teardown():
    print("TEARDOWN")

def test_basic():
    print("I RAN")

def test_temperature_celsius():
    x = temperature.Celsius(40)
    assert_equal(x.getFahrenheit(), 104.0)
    assert_equal(x.units, "Celsius")

def test_temperature_fahreheint():
    x = temperature.Fahrenheit(104.0)
    assert_equal(x.getCelsius(), 40.0)
    assert_equal(x.units, "Fahrenheit") 

def test_temperature_kelvin():
    x = temperature.Kelvin(313.15)
    assert_equal(x.getCelsius(), 40.0)
    assert_equal(x.getValueFahrenheit(), 104.0)

def test_length():
    x = length.Meters(100)
    assert_equal(x.getYards(), 109.35999999999999)
    x = length.Yards(100)
    assert_equal(x.getMeters(), 91.441111923921)
