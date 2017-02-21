#!/usr/bin/python

from csv import *
from package import *
from symbols import *

#
# All information about the ISSI IS61LV6416(L) SRAM chip
# for generation of schematic symbols and footprints
#
class issi_is61lv6416:
    def __init__(this):
        this.pins = CSV("issi_is61lv6416.csv").as_dict()
        print this.pins
        this.packages = [package("SOJ", 44, this.pins), package("TSOP-II", 44, this.pins)]

    def generate_schematic_symbols(this):
        this.generate_schematic_symbol_decoder()
        this.generate_schematic_symbol_io()
        this.generate_schematic_symbol_control()
        this.generate_schematic_symbol_power()

    def get_pin_subset(this, a, b):
        result = {}
        for i in range(a, b):
            result[i] = this.pins[i]
        result[b] = this.pins[b]
        return result

    def generate_schematic_symbol_decoder(this):
        symbol = box( this.get_pin_subset(1,22), this.get_pin_subset(23,44) )
        symbol.export_console()
        symbol.export_kicad("issi_is61lv6416.lib", "ISSI-IS61LV6416", "U")

    def generate_schematic_symbol_io(this):
        print "nothing to do here..."

    def generate_schematic_symbol_control(this):
        print "nothing to do here..."

    def generate_schematic_symbol_power(this):
        print "nothing to do here..."

    def generate_footprints(this):
        print "nothing to do here..."

if __name__ == "__main__":
    ic = issi_is61lv6416()
    ic.generate_schematic_symbols()
    ic.generate_footprints()
