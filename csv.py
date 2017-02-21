#!/usr/bin/python

#
# Read semicolon-separated list of
# pin name/number - pin function assignments
#
class CSV:
    def __init__(this, filename):
        this.pins = {} 

    #
    # Export pin list as dictionary 
    #
    def as_dict(this):
        return this.pins
