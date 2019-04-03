#!/usr/bin/python


#
# Possible pad shapes
#
class Shape:
    CIRCLE = "circle"
    RECT = "rect"


#
# Python class representing a pad in a KiCad footprint
#
class Pad:
    def __init__(
            self,
            designator,
            through_hole=True,
            plated=True,
            shape=Shape.CIRCLE,
            at=(0.0, 0.0),
            size=(0.0, 0.0),
            drill=1.0,
            layers="*.Cu *.Mask *.Paste"
            ):
        self.designator = designator
        self.through_hole = through_hole
        self.plated = plated
        self.shape = shape
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

    def getType(self):
        type = "smd"
        if self.through_hole:
            if self.plated:
                type = "thru_hole"
            else:
                type = "np_thru_hole"
        return type

    # Stringify pad object
    def __str__(self):
        # Only append drill hole size, if the pad is through-hole
        drill = ""
        if self.through_hole:
            drill = "(drill {:.2f}) ".format(self.drill)

        return "  (pad " \
                + str(self.designator) \
                + " " + self.getType() \
                + " " + self.shape \
                + " (at {:.2f} {:.2f}) (size {:.2f} {:.2f}) ".format(
                    self.getX(),
                    self.getY(),
                    self.getSizeX(),
                    self.getSizeY()
                    ) \
                + drill \
                + "(layers " + self.layers + "))"
