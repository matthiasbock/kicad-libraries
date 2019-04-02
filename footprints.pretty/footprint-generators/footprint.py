#!/usr/bin/python


class Footprint:
    def __init__(self, name):
        self.name = name
        self.id = self.name.replace(" ", "_")

        self.elements = []

        self.append(
"""(fp_text reference REF** (at 0 -12.065) (layer F.SilkS)
    (effects (font (size 1 1) (thickness 0.15)))
  )"""
            )
        self.append(
"""(fp_text value "{:s}" (at 0 6.985) (layer F.Fab)
    (effects (font (size 1 1) (thickness 0.15)))
  )""".format(self.name)
            )


    def append(self, element):
        self.elements.append(element)


    def __str__(self):
        return \
"""(module {:s} (layer F.Cu) (tedit 5BE08772)
""".format(self.id) + \
"\n".join([str(element) for element in self.elements]) + \
"\n)"


    def saveAs(self, filename):
        f = open(filename, "w")
        f.write(str(self))
        f.close()
