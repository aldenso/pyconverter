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

    def getmms(self):
        mms = ( self.value * 1000 )
        return mms

    def getcms(self):
        cms = ( self.value * 100 )
        return cms

    def getkms(self):
        kms = ( self.value / 1000 )
        return kms

    def getinches(self):
        inches = (self.value / 0.0254 )
        return inches

    def getfeets(self):
        feets = ( self.value / 0.3048 )
        return feets

    def getyards(self):
        yards = ( self.value * 1.0936 )
        return yards

    def getmiles(self):
        miles = ( self.value / 1000 ) * 0.62137 
        return miles


class Kms(object):
    """
    =================================
    Convert Kilometers to other units
    =================================
    """
    def __init__(self, value):
        self.value = value
        self.units = 'Kms'

    def getmms(self):
        mms = ( self.value * 1000000 )
        return mms

    def getcms(self):
        cms = ( self.value * 100000 )
        return cms

    def getmeters(self):
        meters = ( self.value * 1000 )
        return meters

    def getinches(self):
        inches = ( self.value * 1000 ) / 0.0254 
        return inches

    def getfeets(self):
        feets = ( self.value * 1000 ) / 0.3048 
        return feets

    def getyards(self):
        yards = ( self.value * 1093.6 )
        return yards

    def getmiles(self):
        miles = ( self.value * 0.62137 )
        return miles


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

    def getmms(self):
        mms = ( self.value / 1.0936 ) * 1000
        return mms

    def getcms(self):
        cms = ( self.value / 1.0936 ) * 100
        return cms

    def getmeters(self):
        meters = ( self.value / 1.0936 )
        return meters

    def getkms(self):
        kms = ( self.value / 1093.6 )
        return kms

    def getfeets(self):
        feets = ( self.value * 3 )
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

    def getmeters(self):
        meters = ( self.value * 0.3048 )
        return meters

    def getyards(self):
        yards = ( self.value / 3 )
        return yards
    
    def getinches(self):
        inches = ( self.value * 12 )
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

    def getmeters(self):
        meters = ( self.value * 0.0254 )
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

    def getyards(self):
        yards = ( self.value * 1760 )
        return yards

    def getfeets(self):
        feets = ( self.value * 5280 )
        return feets

    def getkms(self):
        kms = ( self.value / 0.62137 )
        return kms

