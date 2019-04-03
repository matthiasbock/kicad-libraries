#!/usr/bin/python3

import os
from footprint import *
from pad import *
from line import *


#
# Wuerth WR-FPC connector
# SMT, ZIF, bottom contact, 0.50mm pin distance
#
class Wuerth_WR_FPC:
    availablePinCounts = [6, 8, 10, 12, 14, 16, 17, 18, 20, 22, 24, 26, 28, 30, 32, 33, 34, 35, 40, 44, 45, 50]

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
        return "Wuerth {:s}".format(self.getPartNumber())

    #
    # Generate an appropriate filename
    #
    def getFilename(self):
        return "Wuerth_{:s}_1x{:02d}-1MP_P0.5mm_Horizontal".format(self.getPartNumber(), self.pinCount) + ".kicad_mod"

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
        lineWidth      = 0.15

        # Margin between courtyard and silkscreen marking
        margin = {
            "top": innerPadHeight + 0.50,
            # Leave some space for convenient cable plugging
            "bottom": 15.00,
            "left": 0.50,
            "right": 0.50
            }

        # Parameters in the datasheet
        A = pinSpacing * pinCount
        # Component width
        B = A + 4.6
        C = A + 1.1

        # Component height
        D = 5.80

        # Account for the fact that distance is measured from pad center to pad center
        outerToInnerPadDeltaX += outerPadWidth/2    # The inner pad width is already included in the value above
        outerToInnerPadDeltaY += outerPadHeight/2 + innerPadHeight/2

        # Center the footprint
        startX = -outerToInnerPadDeltaX - (self.pinCount/2 - 1/2) * pinSpacing
        startY = 0

        # Add M1
        x = startX
        y = startY
        outerPad = Pad(
                designator = "MP",
                through_hole = False,
                layers = "F.Cu F.Mask",
                plated = True,
                shape = Shape.RECT,
                at = (x, y),
                size = (outerPadWidth, outerPadHeight)
                )
        self.footprint.append(outerPad)
        x += outerToInnerPadDeltaX
        y -= outerToInnerPadDeltaY

        # Add all the pins
        for pin in range(self.pinCount):
            pad = Pad(
                    designator = str(pin+1),
                    through_hole = False,
                    layers = "F.Cu F.Mask",
                    plated = True,
                    shape = Shape.RECT,
                    at = (x, y),
                    size = (innerPadWidth, innerPadHeight)
                    )
            self.footprint.append(pad)
            if pin < self.pinCount-1:
                x += pinSpacing

        # Add M2
        x += outerToInnerPadDeltaX
        y += outerToInnerPadDeltaY
        outerPad = Pad(
                designator = "MP",
                through_hole = False,
                layers = "F.Cu F.Mask",
                plated = True,
                shape = Shape.RECT,
                at = (x, y),
                size = (outerPadWidth, outerPadHeight)
                )
        self.footprint.append(outerPad)

        # Add placement hint to silkscreen
        layer = "F.SilkS"
        x1 = -B/2
        y1 = startY - outerToInnerPadDeltaY + innerPadHeight/2
        x2 = +B/2
        y2 = y1 + D

        lines = [
            Line(x1, y1, x2, y1, layer, lineWidth),
            Line(x2, y1, x2, y2, layer, lineWidth),
            Line(x2, y2, x1, y2, layer, lineWidth),
            Line(x1, y2, x1, y1, layer, lineWidth)
            ]
        for line in lines:
            self.footprint.append(line)

        # Add outline to courtyard layer
        layer = "F.CrtYd"
        x1 -= margin["left"]
        y1 -= margin["top"]
        x2 += margin["right"]
        y2 += margin["bottom"]

        lines = [
            Line(x1, y1, x2, y1, layer, lineWidth),
            Line(x2, y1, x2, y2, layer, lineWidth),
            Line(x2, y2, x1, y2, layer, lineWidth),
            Line(x1, y2, x1, y1, layer, lineWidth)
            ]
        for line in lines:
            self.footprint.append(line)


    #
    # Save the generated footprint to file
    #
    def saveAs(self, filename):
        self.footprint.saveAs(filename)

    def save(self):
        self.saveAs(self.getFilename())



if __name__ == "__main__":
    # Move to footprint storage folder
    os.chdir(os.path.join(os.getcwd(), ".."))

    # Generate footprints for all available connectors in the series
    for pinCount in Wuerth_WR_FPC.availablePinCounts:
        Wuerth_WR_FPC(pinCount).save()
