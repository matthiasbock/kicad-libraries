#!/usr/bin/python

# Regular expressions: for value parsing
import re

# In order to be able to export to KiCad file formats
from kicad import *

#
# Class for reading and parsing ST CubeMX .ioc files
#
class IOC:
    KEY_MCU_PACKAGE = "Mcu.Package"
    KEY_MCU_PIN = "Mcu.Pin"
    KEY_PIN_SIGNAL = ".Signal"
    # number of pins: total, left, bottom, right, top
    PIN_COUNT_BY_PACKAGE = {"LQFP48": [48, 12, 12, 12, 12]}
    ERROR_ATTRIBUTE = -1

    def __init__(self):
        self.content = ""
        self.pinCount = 0
        self.pinCountLeft = 0
        self.pinCountBottom = 0
        self.pinCountRight = 0
        self.pinCountTop = 0
        self.pinNames = []
        self.netNames = []

    #
    # Import .ioc file
    #
    def importFile(self, filename):
        print("Importing CubeMX file "+filename+" ...")
        f = open(filename, "r")
        self.content = f.read()
        f.close()
        self.parse()

    #
    # Returns, whether or not the IOC has a line setting the requested attribute
    #
    def hasKey(self, key):
        return self.content.find(key+"=") > -1

    #
    # Returns the value of the requested key
    #
    def getValue(self, key):
        try:
            result = re.search(".*"+key+"=([a-zA-Z0-9\-\_]*).*", self.content).group(1)
        except AttributeError:
            # Pattern not found
            return self.ERROR_ATTRIBUTE
        return result

    #
    # Parse the MCU package from the IOC file content
    #
    def getPackage(self):
        if not self.hasKey(self.KEY_MCU_PACKAGE):
            return self.ERROR_ATTRIBUTE

        result = self.getValue(self.KEY_MCU_PACKAGE)

        return result

    #
    # Returns the pin count of the selected MCU package
    #
    def getPinCount(self):
        package = self.getPackage()
        if package == self.ERROR_ATTRIBUTE:
            return self.ERROR_ATTRIBUTE

        for key in self.PIN_COUNT_BY_PACKAGE.keys():
            if key == package:
                return self.PIN_COUNT_BY_PACKAGE[key]
    
        return self.ERROR_ATTRIBUTE

    #
    # Parses the imported file to obtain all relevant information
    #
    def parse(self):
        # Determine the pin count of the MCU
        package = self.getPackage()
        if package == self.ERROR_ATTRIBUTE:
            return self.ERROR_ATTRIBUTE
        for key in self.PIN_COUNT_BY_PACKAGE.keys():
            if key == package:
                self.pinCount = self.PIN_COUNT_BY_PACKAGE[key][0]
                self.pinCountLeft = self.PIN_COUNT_BY_PACKAGE[key][1]
                self.pinCountBottom = self.PIN_COUNT_BY_PACKAGE[key][2]
                self.pinCountRight = self.PIN_COUNT_BY_PACKAGE[key][3]
                self.pinCountTop = self.PIN_COUNT_BY_PACKAGE[key][4]

        # Parse the names of the pins in use by the CubeMX project
        self.pinNames = []
        for i in range(self.pinCount):
            value = self.getValue(self.KEY_MCU_PIN+str(i))
            self.pinNames.append(value)

        # Parse the name of the signals
        self.netNames = []
        for i in range(self.pinCount):
            if self.pinNames[i] == self.ERROR_ATTRIBUTE:
                self.netNames.append(self.ERROR_ATTRIBUTE)
                continue

            signal = self.getValue(self.pinNames[i]+self.KEY_PIN_SIGNAL)
            if signal != self.ERROR_ATTRIBUTE:
                if signal.find("S_TIM") == 0:
                    signal = signal[2:]
                self.netNames.append(signal)
                print(self.pinNames[i]+" used as "+self.netNames[i])

    #
    # Export the MCU configuration as KiCad symbol
    #
    def generateKicadSymbol(self):
        symbol = KicadSymbol()
        return symbol
