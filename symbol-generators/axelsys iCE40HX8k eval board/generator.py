#!/usr/bin/python3

import sys
sys.path.append("..")
from kicad_symbols import *

name = "axelsys-iCE40HX8k-eval-board"

pinoutFile = "j1.csv"

# Import pinout from file
f = open(pinoutFile)
csv = f.read()
f.close()

# Parse all pins from the CSV
pins = []
for line in csv.split("\n"):
    s = line.split(";")
    try:
        number = int(s[0])
        designator = s[1]
        pinType = s[2]
    except:
        continue

    #print("Pin " + str(number) + ": " + designator + ", Type: " + pinType)
    pins.append( {"number": number, "designator": designator, "pinType": pinType} )

#print( pins )


# Create new symbol
symbol = Symbol(name, "B") 

startY = 550
y = startY
for pin in pins:
    if pin["number"] % 2 != 0:
        x = -350
        o = PIN_ORIENTATION_RIGHT
        y -= 100
    else:
        x = 350
        o  = PIN_ORIENTATION_LEFT

    newPin = Pin(number=pin["number"], designator=pin["designator"], x=x, y=y, orientation=o, pinType=pin["pinType"])
    symbol.addElement(newPin)

bottomY = y

symbol.addElement( Rectangle(-250, startY, 250, bottomY-100) )
symbol.addElement( Text("J1", 200, startY+50) )
symbol.setTopY( startY+50 )
symbol.setBottomY( bottomY-150 )

print( str(symbol) )

