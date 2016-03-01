from nose.tools import *
from pyconverter import length

def test_Meters():
	mms = length.Meters(1)
	assert_equal(mms.getmms(), 1000)
	cms = length.Meters(1.5)
	assert_equal(cms.getcms(), 150)
	kms = length.Meters(1300)
	assert_equal(kms.getkms(), 1.3)
	ins = length.Meters(1)
	assert_equal(ins.getinches(), 39.37007874015748)
	fts = length.Meters(2)
	assert_equal(fts.getfeets(), 6.561679790026246)
	yds = length.Meters(100)
	assert_equal(yds.getyards(), 109.35999999999999)
	mis = length.Meters(1500)
	assert_equal(mis.getmiles(), 0.932055)


def test_Kms():
	mms = length.Kms(0.01)
	assert_equal(mms.getmms(), 10000)
	cms = length.Kms(1)
	assert_equal(cms.getcms(), 100000)
	meters = length.Kms(1.3)
	assert_equal(meters.getmeters(), 1300)
	ins = length.Kms(1)
	assert_equal(ins.getinches(), 39370.078740157485)
	fts = length.Kms(1)
	assert_equal(fts.getfeets(), 3280.839895013123)
	yds = length.Kms(1)
	assert_equal(yds.getyards(), 1093.6)
	mis = length.Kms(2)
	assert_equal(mis.getmiles(), 1.24274)


def test_Yards():
	mms = length.Yards(100)
	assert_equal(mms.getmms(), 91441.111923921)
	cms = length.Yards(100)
	assert_equal(cms.getcms(), 9144.1111923921)
	meters = length.Yards(100)
	assert_equal(meters.getmeters(), 91.441111923921)
	kms = length.Yards(1093.6)
	assert_equal(kms.getkms(), 1)

def test_Miles():
	kms = length.Miles(1)
	assert_equal(kms.getkms(), 1.6093470878864444)