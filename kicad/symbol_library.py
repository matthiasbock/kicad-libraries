#!/usr/bin/python

class KicadSymbolLibrary:
    def __init__(self):
        self.symbols = []

    def addSymbol(self, symbol):
        self.symbols.append(symbol)

    def __str__(self):
        lib = "EESchema-LIBRARY Version 2.3\n#encoding utf-8\n"
        for symbol in self.symbols:
            lib += str(symbol)
        lib += "#\n#End Library"
        return lib
