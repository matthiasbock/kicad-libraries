#!/usr/bin/python

class KicadSymbol:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.pinCountLeft = 0
        self.pinCountBottom = 0
        self.pinCountRight = 0
        self.pinCountTop = 0

    def generateFromCubeMX(self, cubefile):
        self.pinCountLeft = cubefile.pinCountLeft
        self.pinCountBottom = cubefile.pinCountBottom
        self.pinCountRight = cubefile.pinCountBottom
        self.pinCountTop = cubefile.pinCountTop

    def __str__(self):
        symbol = "DEF L298 U 0 40 Y Y 1 F N\n"
        symbol += "ENDDEF\n"
        return symbol
