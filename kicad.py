#!/usr/bin/python
#
# This library enables generation of KiCAD files
#

#
# KiCAD file formats overview:
# http://kicad-pcb.org/help/file-formats/
#
# KiCAD file format description:
# https://www.compuphase.com/electronics/LibraryFileFormats.pdf
#

#
# Schematic symbol library
#
class kicad_symbol_library:
    def __init__(this):
        this.symbols = []

    def add(this, symbol):
        this.symbols.append(symbol)

    def __str__(this):
        lib = """EESchema-LIBRARY Version 2.3
#encoding utf-8
#
# KiCAD schematic symbol library
# generated by ScriptCAD
#
"""
        for symbol in this.symbols:
            lib += str(symbol) 
        lib += """#
# End Library
#
"""
        return lib

    def save_as(this, filename):
        f = open(filename, "w")
        f.write(str(this))
        f.close()

#
# Schematic symbol
#
class kicad_symbol:
    def __init__(this, name, prefix):
        this.name = name
        this.symbol_prefix = prefix

    def __str__(this):
        symbol = "DEF " \
               + str(this.name) + " " \
               + str(this.symbol_prefix) \
               + "\n"
        symbol += "ENDDEF\n"
        return symbol
