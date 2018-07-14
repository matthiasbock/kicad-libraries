#!/usr/bin/python

from sys import argv, exit
from cubemx import *
from kicad import *


filename = argv[1]

iocFile = IOC()
iocFile.importFile(filename)

print("=====")

mcu = iocFile.generateKicadSymbol()
print(str(mcu))

print("=====")

lib = KicadSymbolLibrary()
lib.addSymbol(mcu)
print(str(lib))

print("=====")

sch = KicadSchematic()
sch.addLibrary("test")
sch.addSymbol(symbol=mcu, reference="U1", x=5000, y=5000)
print(str(sch))
