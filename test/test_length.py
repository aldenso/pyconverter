from nose.tools import *
from pyconverter import length

def test_Meters():
    x = length.Meters(100)
    assert_equal(x.getyards(), 109.35999999999999)
    x = length.Meters(1.5)
    assert_equal(x.getcms(), 150)

def test_Kms():
	x = length.Kms(1.3)
	assert_equal(x.getmeters(), 1300)
	x = length.Kms(0.1)
	assert_equal(x.getcms(), 10000)
	x = length.Kms(2)
	assert_equal(x.getmiles(), 1.24274)
	x = length.Kms(1)
	assert_equal(x.getyards(), 1093.6)

def test_Yards():
    x = length.Yards(100)
    assert_equal(x.getmeters(), 91.441111923921)
    x = length.Yards(1093.6)
    assert_equal(x.getkms(), 1)

def test_Miles():
	x = length.Miles(1)
	assert_equal(x.getkms(), 1.6093470878864444)