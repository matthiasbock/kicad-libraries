#!/usr/bin/python

# Regular expressions: for value parsing
import re

#
# Class for reading and parsing ST CubeMX .ioc files
#
class IOC:
    KEY_MCU_PACKAGE = "Mcu.Package"

    def __init__(self):
        self.content = ""

    #
    # Import .ioc file
    #
    def importFile(self, filename):
        f = open(filename, "r")
        self.content = f.read()
        f.close()

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
            result = re.search(".*"+key+"=([a-zA-Z0-9]*).*", self.content).group(1)
        except AttributeError:
            # Pattern not found
            return ""
        return result

    #
    # Parse the MCU package from the IOC file content
    #
    def getPackage(self):
        if not self.hasKey(self.KEY_MCU_PACKAGE):
            return ""

        result = self.getValue(self.KEY_MCU_PACKAGE)

        return result
