#!/usr/bin/python

from csv import *
from package import * 

#
# All information about the ISSI IS61LV6416(L) SRAM chip
# for generation of schematic symbols and footprints
#
class issi_is61lv6416:
    def __init__(this):
        pins = CSV("issi_is61lv6416.csv").as_dict()
        this.packages = [Package("SOJ", 44, pins), Package("TSOP-II", 44, pins)]

    def generate_schematic_symbols(this):
        this.generate_schematic_symbol_decoder()
        this.generate_schematic_symbol_io()
        this.generate_schematic_symbol_control()
        this.generate_schematic_symbol_power()

    def generate_footprints(this):
        print "nothing to do here..."

if __name__ == "__main__":
    ic = issi_is61lv6416()
    ic.generate_schematic_symbols()
    ic.generate_footprints()
