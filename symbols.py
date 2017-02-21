#!/usr/bin/python

from kicad import *

#
# Basic schematic symbol:
# a rectangular box with pins left, right, top and bottom
# (latter three optional)
#

def print_pins(pins):
    for pin in pins:
        print "* "+str(pin)+": "+str(pins[pin])

class box:
    def __init__(this, pins_left, pins_right=None, pins_top=None, pins_bottom=None):
        this.pins_left   = pins_left
        this.pins_right  = pins_right
        this.pins_top    = pins_top
        this.pins_bottom = pins_bottom

    def export_console(this):
        print "Box!"
        if this.pins_left != None:
            print "Pins left:"
            print_pins(this.pins_left)
        if this.pins_right != None:
            print "Pins right:"
            print_pins(this.pins_right)
        if this.pins_top != None:
            print "Pins top:"
            print_pins(this.pins_top)
        if this.pins_bottom != None:
            print "Pins bottom:"
            print_pins(this.pins_bottom)

    def export_kicad(this, filename, name, symbol_prefix):
        symbol = kicad_symbol(name, symbol_prefix)
        lib = kicad_symbol_library()
        lib.add(symbol)
        lib.save_as(filename)
