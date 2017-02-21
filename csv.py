#!/usr/bin/python

#
# Read semicolon-separated list of
# pin name/number - pin function assignments
#
class CSV:
    def __init__(this, filename):
        this.pins = {}
        counter = 0
        for line in open(filename, "r").read().split("\n"):
            if (len(line.strip()) == 0):
                continue
            counter += 1
            field = line.split(";")
            if (len(field) < 2):
                print "Error in line "+str(counter)+": At least two fields are required"
                continue
            this.pins[field[0]] = field[1]

    #
    # Export pin list as dictionary 
    #
    def as_dict(this):
        return this.pins
