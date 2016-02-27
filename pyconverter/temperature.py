"""
Classes and functions for temperature convertion units
Units: Celsius, Fahrenheit and Kelvin.
=====================================
C = K - 273.15
C = (F - 32) * (5/9)
F = C * (9/5) + 32
F = ( K - 273.15 ) * (9/5) + 32
K = C + 273.15
K = ( F - 32 ) * (5/9) + 273.15 
=====================================
"""

class Celsius(object):
    """ Convert Celsius to Fahrenheit and Kelvin """
    def __init__(self, value):
        self.value = value
        self.units = 'Celsius'

    def getFahrenheit(self):
        f = self.value * (9/5) +32
        return f

    def getKelvin(self):
        k = self.value + 273.15
        return k

class Fahrenheit(object):
    """ Convert Fahrenheit to Celsius and Kelvin """
    def __init__(self, value):
        self.value = value
        self.units = 'Fahrenheit'

    def getCelsius(self):
        c = ( self.value - 32 ) * ( 5 / 9 )
        return c

    def getKelvin(self):
        c = ( self.value - 32 ) * ( 5 / 9 ) + 273.15
        return c

class Kelvin(object):
    """ Convert Kelvin to Celsius and Fahrenheit """
    def __init__(self, value):
        self.value = value
        self.units = 'Kelvin'

    def getCelsius(self):
        c = ( self.value - 273.15 )
        return c

    def getFahrenheit(self):
        f = ( self.value - 273.15 ) * ( 9 / 5 ) + 32
        return f
