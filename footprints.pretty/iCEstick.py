#!/usr/bin/python

# Point of origin (connector J3, pad 1, net 3V3)
x = 0.0
y = 0.0

drillDiameter = 1.0
padWidth = 1.6


from os.path import exists
from pads import *

filename="iCEstick.kicad_mod"

header = ""
footer = ""

if exists(filename):
    # Read existing footprint
    f = open(filename)
    footprint = f.read()
    f.close()
    
    # Find the end of the header
    headerEndIndex = footprint.find("(pad ")
    header = footprint[:headerEndIndex]
    
    # Find the end of the pads list
    lastPadIndex = headerEndIndex
    while (footprint.find("(pad ", lastPadIndex) > -1):
        lastPadIndex = footprint.find("(pad ", lastPadIndex) + 5
    
    footerStartIndex = footprint.find("))", lastPadIndex) + 2
    footer = footprint[footerStartIndex:]

if header.find("TE-Connectivity") < 0:
    header = \
"""(module iCEstick (layer F.Cu) (tedit 5BD73D6F)
  (fp_text reference REF** (at 0 -12.7) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value iCEstick (at 0 25.4) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
"""
    footer = ")"

#
# Generate pads according to schematic drawing
#

designators_j1 = ["3V3", "GND"] + [str(n) for n in range(112,120)]

designators_j2 = [ \
                    [str(n) for n in range(78,82)] + ["GND", "3V3"], \
                    ["87", "88", "90", "91", "GND", "3V3"] \
                 ]

designators_j3 = ["3V3", "GND", "62", "61", "60", "56", "48", "47", "45", "44"]

#
# J1 connector pad list
#
pads_j1 = []
oldX = x
oldY = y
y -= 21.81
for i in range(10):
    # The first pad is a rectangle, the remaining ones are circular
    if (i == 0):
        shape = Shape.RECT
    else:
        shape = Shape.CIRCLE
 
    # Create pad object
    newPad = Pad(
            designator = designators_j1[i],
            through_hole = True,
            plated = True,
            shape = shape,
            at = (x, y),
            size = (padWidth, padWidth),
            drill = drillDiameter
            )
    pads_j1 += [newPad]
    x -= 2.54

#
# J2 connector pad list
#
pads_j2 = []
x = oldX - 5.80
newY = oldY - 21.81 + 4.49 + 5*2.54
y = newY
for i in range(6):
    # The first pad is a rectangle, the remaining ones are circular
    if (i == 0):
        shape = Shape.RECT
    else:
        shape = Shape.CIRCLE
 
    # Create pad object
    newPad = Pad(
            designator = designators_j2[0][i],
            through_hole = True,
            plated = True,
            shape = shape,
            at = (x, y),
            size = (padWidth, padWidth),
            drill = drillDiameter
            )
    pads_j2 += [newPad]
    y -= 2.54

# Second (inner) row of pins of J2
x -= 2.54
y = newY
for i in range(6):
    # Create pad object
    newPad = Pad(
            designator = designators_j2[1][i],
            through_hole = True,
            plated = True,
            shape = Shape.CIRCLE,
            at = (x, y),
            size = (padWidth, padWidth),
            drill = drillDiameter
            )
    pads_j2 += [newPad]
    y -= 2.54

#
# J3 connector pad list
#
pads_j3 = []
x = oldX
y = oldY
for i in range(10):
    # The first pad is a rectangle, the remaining ones are circular
    if (i == 0):
        shape = Shape.RECT
    else:
        shape = Shape.CIRCLE
 
    # Create pad object
    newPad = Pad(
            designator = designators_j3[i],
            through_hole = True,
            plated = True,
            shape = shape,
            at = (x, y),
            size = (padWidth, padWidth),
            drill = drillDiameter
            )
    pads_j1 += [newPad]
    x -= 2.54

# Make a list of all pads
pads = pads_j1 + pads_j2 + pads_j3

# Compose new footprint from header, pads and footer
newFootprint = header
for pad in pads:
    newFootprint += str(pad) + "\n"
newFootprint += footer.strip()

# Print generated footprint to screen
print(newFootprint)

# Save generated footprint to file
f = open(filename, "w")
f.write(newFootprint)
f.close()
