#!/usr/bin/python

from os.path import exists
from pad import *


filename="Bourns-CAY16.kicad_mod"


#
# Constant parts of the file
#
header = """(module Bourns-CAY16 (layer F.Cu) (tedit 5C599271)
  (fp_text reference REF** (at 0 -8.255) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value Bourns-CAY16 (at 0 8.89) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )"""

footer = ")"


#
# Values from the datasheet
#
B = 3.2     # Package width
D = 1.6     # Package height
a = 0.8     # Spacing between pads in Y direction
b = 0.4     # Pad width
p = 0.8     # Distance between neighbouring pads' centers
f = 2.6     # Total height in Y direction


#
# Generate pads according to schematic drawing
#

# Pad parameters
padCount = 8
padWidth = b
padHeight = (f-a)/2.0
padSpacingX = p
padSpacingY = padHeight + a

# Array of pads
pads = []

# Start position (first pad)
x = 0.0
y = padSpacingY/2.0

for i in range(int(padCount/2)):
    # Create pad object
    newPad = Pad(
            designator = str(i+1),
            through_hole = False,
            plated = True,
            shape = Shape.RECT,
            at = (x, y),
            size = (padWidth, padHeight),
            layers = "F.Cu F.Paste F.Mask"
            )
    # Append pad to list of pads
    pads += [newPad]
    x += padSpacingX

# Top line of pads
y -= padSpacingY

for i in range(int(padCount/2)):
    x -= padSpacingX
    # Create pad object
    newPad = Pad(
            designator = str(int(padCount/2)+1+i),
            through_hole = False,
            plated = True,
            shape = Shape.RECT,
            at = (x, y),
            size = (padWidth, padHeight),
            layers = "F.Cu F.Paste F.Mask"
            )
    # Append pad to list of pads
    pads += [newPad]


#
# Compose new footprint
#
newFootprint = header.strip() + "\n"
for pad in pads:
    newFootprint += str(pad) + "\n"
newFootprint += footer.strip()

# Print generated footprint to screen
print(newFootprint)

# Save generated footprint to file
f = open(filename, "w")
f.write(newFootprint)
f.close()
