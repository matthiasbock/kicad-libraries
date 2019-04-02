#!/usr/bin/python3

from footprint import *
from pad import *


#
# Wuerth WR-FPC connector
# SMT, ZIF, bottom contact, 0.50mm pin distance
#
class Wuerth_WR_FPC:
    def __init__(self, pinCount):
        self.pinCount = pinCount
        self.generate()

    #
    # Generate the official Wuerth part number, which depends on the pin count
    #
    def getPartNumber(self):
        return "6871{:02d}149022".format(self.pinCount)

    #
    # Generate a footprint name
    #
    def getName(self):
        return "Wuerth WR-FPC {:s}".format(self.getPartNumber())

    #
    # Add some primitives to the canvas
    #
    def generate(self):
        self.footprint = Footprint(self.getName())

        # Parameters
        outerPadWidth  = 2.00
        outerPadHeight = 1.80
        innerPadWidth  = 0.30
        innerPadHeight = 1.30
        outerToInnerPadDeltaX = 0.80
        outerToInnerPadDeltaY = 1.20
        pinSpacing     = 0.50

        # Account for the fact that distance is measured from pad center to pad center
        outerToInnerPadDeltaX += outerPadWidth/2    # The inner pad width is already included in the value above
        outerToInnerPadDeltaY += outerPadHeight/2 + innerPadHeight/2

        # KiCad increases Y downwards
        outerToInnerPadDeltaY = -outerToInnerPadDeltaY

        # Generate pads
        x = 0
        y = 0
        outerPad = Pad(
                designator = "M1",
                through_hole = False,
                plated = True,
                shape = Shape.RECT,
                at = (x, y),
                size = (outerPadWidth, outerPadHeight)
                )
        self.footprint.append(outerPad)
        x += outerToInnerPadDeltaX
        y += outerToInnerPadDeltaY

        for pin in range(self.pinCount):
            pad = Pad(
                    designator = str(pin+1),
                    through_hole = False,
                    plated = True,
                    shape = Shape.RECT,
                    at = (x, y),
                    size = (innerPadWidth, innerPadHeight)
                    )
            self.footprint.append(pad)
            if pin < self.pinCount-1:
                x += pinSpacing

        x += outerToInnerPadDeltaX
        y -= outerToInnerPadDeltaY

        outerPad = Pad(
                designator = "M2",
                through_hole = False,
                plated = True,
                shape = Shape.RECT,
                at = (x, y),
                size = (outerPadWidth, outerPadHeight)
                )
        self.footprint.append(outerPad)

    #
    # Save the generated footprint to file
    #
    def saveAs(self, filename):
        self.footprint.saveAs(filename)

    def save(self):
        self.saveAs(self.getName().replace(" ","_") + ".kicad_mod")



if __name__ == "__main__":
    header = Wuerth_WR_FPC(20)
    header.save()
