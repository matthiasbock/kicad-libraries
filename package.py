#!/usr/bin/python

#
# One chip can be available in several packages.
# Each package has a name and
# may have it's own unique pin assignment.
#

class package:
    #
    # Initialize with package name, e.g. "TQFP" and pins
    # Pins are a dictionary, where the key is the pin name and the value is the pin function. 
    #
    def __init__(this, name, pin_count, pins):
        this.name = name
        this.pin_count = pin_count
        this.pins = pins

    def get_name(this):
        return this.name

    def get_pin_count(this):
        return pin_count

    def get_pin_name(this, pin_number):
        return this.pins[pin_number]

    def get_pin_by_name(this, pin_name):
        return this.pins.index(pin_name)
