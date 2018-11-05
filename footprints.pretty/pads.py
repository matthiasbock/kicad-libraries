#!/usr/bin/python

#
# Python class representing a pad in a KiCad footprint
#
class Pad:
    def __init__(
            self,
            designator,
            type="thru_hole circle",
            at=(0.0, 0.0),
            size=(0.0, 0.0),
            drill=1.0,
            layers="*.Cu *.Mask"
            ):
        self.designator = designator
        self.type = type
        self.at = at
        self.size = size
        self.drill = drill
        self.layers = layers

    def getX(self):
        return self.at[0]

    def getY(self):
        return self.at[1]

    def getSizeX(self):
        return self.size[0]

    def getSizeY(self):
        return self.size[1]

    # Stringify pad object
    def __str__(self):
        return "  (pad " \
                + str(self.designator) \
                + " " \
                + self.type \
                + " (at " + str(self.getX()) + " " + str(self.getY()) + ") " \
                + "(size " + str(self.getSizeX()) + " " + str(self.getSizeY()) + ") " \
                + "(drill " + str(self.drill) + ") " \
                + "(layers " + self.layers + "))"
