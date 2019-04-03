#!/usr/bin/python


class Line:
    def __init__(self, x1, y1, x2, y2, layer, lineWidth):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.layer = layer
        self.lineWidth = lineWidth

    def __str__(self):
        return """(fp_line (start {:.1f} {:.1f}) (end {:.1f} {:.1f}) (layer {:s}) (width {:.2f}))""" \
                .format(self.x1, self.y1, self.x2, self.y2, self.layer, self.lineWidth)
