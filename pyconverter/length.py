"""
Classes and functions for length convertion units
Measurement Systems: 
    Metric System
    US Customary Units/Imperial System
"""

class Meters(object):
    """
    =============================
    Convert meters to other units
    =============================
    m = yd / 1.0936
    m = ft / 0.3048
    m = in * 0.0254
    _____________________________
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Meters'

    def getKms(object):
        kms = ( self.value / 1000 )
        return kms

    def getYards(self):
        yards = self.value * 1.0936
        return yards

    def getFeets(self):
        feets = ( self.value / 0.3048 )
        return feets

    def getInches(self):
        inches = (self.value / 0.0254 )
        return inches

class Kms(object):
    """
    =================================
    Convert Kilometers to other units
    =================================
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Kms'

    def getMeters(self):
        meters = self.value * 1000
        return meters

class Yards(object):
    """
    ============================
    Convert yards to other units
    ============================
    yd = m * 1.0936
    yd = ft / 3
    ___________________________
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Yards'

    def getMeters(self):
        meters = self.value / 1.0936
        return meters

    def getFeets(self):
        feets = self.value * 3
        return feets

class Feets(object):
    """
    ============================
    Convert Feets to other units
    ============================
    ft = m / 0.3038
    ft = yd * 3
    ft = in / 12
    ____________________________
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Feets'

    def getMeters(self):
        meters = self.value * 0.3048
        return meters

    def getYards(self):
        yards = ( self.value / 3 )
        return yards
    
    def getInches(self):
        inches = self.value * 12
        return inches

class Inches(object):
    """
    =============================
    Convert Inches to other units
    =============================
    in = m / 0.0254
    _____________________________
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Inches'

    def getMeters(self):
        meters = self.value * 0.0254
        return meters

class Miles(object):
    """
    ============================
    Convert Miles to other units
    ============================
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Miles'

    def getYards(self):
        yards = self.value * 1760
        return yards

    def getFeets(self):
        feets = self.value * 5280
        return feets

