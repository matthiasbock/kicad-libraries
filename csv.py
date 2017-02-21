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
            counter += 1

            if (len(line.strip()) == 0):
                print "Ignoring empty line "+str(counter)
                continue

            field = line.split(";")
            if (len(field) < 2):
                print "Error in line "+str(counter)+": At least two fields are required"
                continue
            if (len(field[0].strip()) == 0 or len(field[1].strip()) == 0):
                print "Error in line "+str(counter)+": At least two non-empty fields are required"
                continue

            # try parsing first field as integer
            try:
                this.pins[int(field[0])] = field[1]
            except:
                this.pins[field[0]] = field[1]

    #
    # Export pin list as dictionary 
    #
    def as_dict(this):
        return this.pins
