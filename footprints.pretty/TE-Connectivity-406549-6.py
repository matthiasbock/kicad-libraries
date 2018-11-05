#!/usr/bin/python

from os.path import exists
from pads import Pad

filename="TE-Connectivity-406549-6.kicad_mod"

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
"""(module TE-Connectivity-406549-6 (layer F.Cu) (tedit 5BE08772)
  (fp_text reference REF** (at 0 -12.065) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_text value "TE Connectivity 406549-6" (at 0 6.985) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )
  (fp_line (start -9.525 5.08) (end 9.525 5.08) (layer F.CrtYd) (width 0.15))
  (fp_line (start 9.525 -10.795) (end -9.525 -10.795) (layer F.CrtYd) (width 0.15))
  (fp_line (start -9.525 -10.795) (end -9.525 5.08) (layer F.CrtYd) (width 0.15))
  (fp_line (start 9.525 5.08) (end 9.525 -10.795) (layer F.CrtYd) (width 0.15))
  
  (fp_line (start -9.525 5.08) (end 9.525 5.08) (layer F.SilkS) (width 0.15))
  (fp_line (start 9.525 -10.795) (end -9.525 -10.795) (layer F.SilkS) (width 0.15))
  (fp_line (start -9.525 -10.795) (end -9.525 5.08) (layer F.SilkS) (width 0.15))
  (fp_line (start 9.525 5.08) (end 9.525 -10.795) (layer F.SilkS) (width 0.15))
"""
    footer = \
"""
  (model /home/code/kicad/libraries/Matthias/3d-models/te-406549-6-r4-3d.stp
    (offset (xyz 0 -5.28 6.5))
    (scale (xyz 1 1 1))
    (rotate (xyz -90 0 0))
  )
)
"""

#
# Generate pads according to schematic drawing
#

# Point of origin (H2 pad)
x = -12.7/2
y = 0.0

# Two holes
H2 = Pad(
        designator = "H2",
        type = "np_thru_hole circle",
        at = (x, y),
        size = (3.5, 3.5),
        drill = 3.5
        )

H1 = Pad(
        designator = "H1",
        type = "np_thru_hole circle",
        at = (H2.getX() + 12.7, H2.getY()),
        size = H2.size,
        drill = H2.drill
        )

# Two shielding connectors
SH2 = Pad(
        designator = "SH2",
        at = (H2.getX() - 1.78, H2.getY() - 3.43),
        size = (2.4, 2.4),
        drill = 1.57 + 0.08
        )

SH1 = Pad(
        designator = "SH1",
        at = (H1.getX() + 1.78, H1.getY() - 3.43),
        size = SH2.size,
        drill = SH2.drill
        )

# Create empty pad list
pad = [None for i in range(13)]

# Begin with pad 8
pad[8] = Pad(
            designator = 8,
            at = (H2.getX() + 2.79, H2.getY() - 2.54 - 1.78),
            size = (1.6, 1.6),
            drill = 0.89 + 0.08
            )

# Generate even pad numbers
counter = 1
for i in [6, 4, 2]:
    pad[i] = Pad(
                designator = i,
                at = (pad[8].getX() + counter*2.03, pad[8].getY()),
                size = pad[8].size,
                drill = pad[8].drill
                )
    counter += 1

# Generate odd pad numbers
counter = 1
for i in [7, 5, 3, 1]:
    pad[i] = Pad(
                designator = i,
                at = (pad[8].getX() + (counter-0.5)*2.03, H2.getY() - 2.54),
                size = pad[8].size,
                drill = pad[8].drill 
                )
    counter += 1

# Add LED pads
pad[12] = Pad(
            designator = 12,
            at = (H2.getX() - 0.51, H2.getY() - 9.14),
            size = pad[8].size,
            drill = pad[8].drill
            )

pad[11] = Pad(
            designator = 11,
            at = (pad[12].getX() + 2.29, pad[12].getY()),
            size = pad[12].size,
            drill = pad[12].drill
            )

pad[9] = Pad(
            designator = 9,
            at = (pad[12].getX() + 13.72, pad[12].getY()),
            size = pad[12].size,
            drill = pad[12].drill
            )

pad[10] = Pad(
            designator = 10,
            at = (pad[9].getX() -2.29, pad[12].getY()),
            size = pad[12].size,
            drill = pad[12].drill
            )

# Make a list of all pads
pads = [H1, H2, SH1, SH2]
for i in range(12):
    if not pad[i+1] is None:
        pads.append(pad[i+1])

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
