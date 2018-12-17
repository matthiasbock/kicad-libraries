#!/usr/bin/python3

#
# Adds a pin to the symbol
#
class Pin:
    def __init__(self, number, designator, x, y, orientation, pinType):
        self.number = number
        self.designator = designator
        self.x = x
        self.y = y
        self.orientation = orientation
        self.pinType = pinType

    def __str__(self):
        return "X " + self.designator + " " + str(self.number) + " " + str(self.x) + " " + str(self.y) + " 100 " + self.orientation + " 50 50 1 1 " + self.pinType + "\n"


#
# Some helper constants for the configurable pin attributes
#
PIN_ORIENTATION_LEFT = "L"
PIN_ORIENTATION_RIGHT = "R"

PIN_TYPE_INPUT = "I"
PIN_TYPE_OUTPUT = "O"
PIN_TYPE_BIDIRECTIONAL = "B"
PIN_TYPE_PASSIVE = "P"


#
# Adds a text label to the symbol
#
class Text:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.text = text

    def __str__(self):
        return "T 0 " + str(self.x) + " " + str(self.y) + " 50 0 1 0 " + self.text + " Normal 0 C C\n"


#
# Adds a (yellow filled) rectangle to the symbol
#
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return "S " + str(self.x1) + " " + str(self.y1) + " " + str(self.x2) + " " + str(self.y2) + " 0 1 0 f\n"


#
# KiCad schematic symbol
#
class Symbol:
    def __init__(self, name, designator):
        self.name = name
        self.designator = designator
        self.elements = []

    def addElement(self, element):
        self.elements.append(element)

    def setTopY(self, y):
        self.topY = y

    def setBottomY(self, y):
        self.bottomY = y

    def __str__(self):
        symbol = "#\n# " + self.name + "\n#\n"
        symbol += "DEF " + self.name + " " + self.designator + " 0 40 Y Y 1 F N\n"
        symbol += "F0 \"" + self.designator + "\" -200 " + str(self.topY) + " 50 H V C CNN\n"
        symbol += "F1 \"" + self.name + "\" 50 " + str(self.bottomY) + " 50 H V C CNN\n"
        symbol += "F2 \"\" 0 0 50 H I C CNN\n"
        symbol += "F3 \"\" 0 0 50 H I C CNN\n"
        symbol += "DRAW\n"

        for element in self.elements:
            symbol += str(element)

        symbol += "ENDDRAW\n"
        symbol += "ENDDEF\n"
        return symbol
