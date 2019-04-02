#!/usr/bin/python3

from footprint import *
from pad import *


#
# Wuerth WR-FPC SMT ZIF HORIZONTAL BOTTOM CONTACT, 0.50MM 
#
class Wuerth_WR_FPC:
    def __init__(self, pinCount):
        self.pinCount = pinCount
        self.header = Footprint(self.getName())

    def getName(self):
        return "Wuerth WR-FPC {:s}".format(self.getPartNumber())

    #
    # Generate the official Wuerth part number, which depends on the pin count
    #
    def getPartNumber(self):
        return "6871{:02d}149022".format(self.pinCount)

    #
    # Save the generated footprint to file
    #
    def saveAs(self, filename):
        self.header.saveAs(filename)

    def save(self):
        self.saveAs(self.getName().replace(" ","_") + ".kicad_mod")



if __name__ == "__main__":
    header = Wuerth_WR_FPC(20)
    header.save()
