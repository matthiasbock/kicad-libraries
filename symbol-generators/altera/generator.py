#!/usr/bin/python3

import sys
sys.path.append("..")
from kicad_symbols import *

name = "EPM3064A"

pinoutFile = "epm3064a-tc44.csv"

# Import pinout from file
f = open(pinoutFile)
csv = f.read()
f.close()

# Parse all pins from the CSV
pins = []
io_counter = 0
for line in csv.split("\n"):
    s = line.split(";")
    try:
        number = int(s[0])
        designator = s[1]
        # Numerize I/O pins
        p = designator.find("I/O")
        if p > -1:
            designator = designator[:p+3] + str(io_counter) + designator[p+3:]
            io_counter += 1
        pinType = s[2]
    except:
        continue

    #print("Pin " + str(number) + ": " + designator + ", Type: " + pinType)
    pins.append( {"number": number, "designator": designator, "pinType": pinType} )

print(pins)

# Create new symbol
symbol = Symbol(name, "B") 

startY = 550
y = startY
for pin in pins:
    # Voltage supply pins
    if pin["designator"].find("VCC") > -1:
        o = PIN_DIRECTION_DOWN
    # Ground pins
    elif pin["designator"].find("GND") > -1:
        o = PIN_DIRECTION_UP
    # I/O pins
    elif pin["number"] < 16:
        x = -350
        o = PIN_DIRECTION_RIGHT
        y -= 100
    else:
        x = 350
        o  = PIN_DIRECTION_LEFT
        y -= 100
    if pin["number"] == 18:
        y = startY

    pin["designator"] = pin["designator"].replace("I/O", "IO")

    newPin = Pin(number=pin["number"], designator=pin["designator"], x=x, y=y, direction=o, pinType=pin["pinType"])
    symbol.addElement(newPin)

bottomY = y

symbol.addElement( Rectangle(-250, startY, 250, bottomY-100) )
symbol.addElement( Text("J1", 200, startY+50) )
symbol.setTopY( startY+50 )
symbol.setBottomY( bottomY-150 )

print( str(symbol) )
