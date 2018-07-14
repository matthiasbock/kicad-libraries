#!/usr/bin/python

from sys import argv, exit
from cubemx import *
from kicad import *


filename = argv[1]

iocFile = IOC()
iocFile.importFile(filename)

print("=====")

mcu = KicadSymbol()
mcu.generateFromCubeMX(iocFile)
print(str(mcu))

print("=====")

lib = KicadSymbolLibrary()
lib.addSymbol(mcu)
print(str(lib))
#lib.saveFile("test.lib")

exit(0)

sch = KicadSchematic()
sch.referenceLibrary("test.lib")
sch.addSymbol(mcu, x, y)
