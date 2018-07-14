#!/usr/bin/python

class KicadSchematic:
    def __init__(self):
        self.libraries = []
        self.symbols = []

    def addLibrary(self, lib):
        self.libraries.append(lib)

    def addSymbol(self, symbol, reference, x, y):
        self.symbols.append(symbol)

    def __str__(self):
        # Header
        schematic = "EESchema Schematic File Version 2\n"

        # Libraries
        for lib in self.libraries:
            schematic += "LIBS:"+lib+"\n"

        # Metadata
        schematic += """EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 7 13
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
"""

        # Symbols
#        for symbol in self.symbols:
#            component = KicadComponent(symbol)
            #schematic += symbol.instantiateComponent("U1", 5250, 3050)

        # Footer
        schematic += "$EndSCHEMATC\n"

        return schematic
