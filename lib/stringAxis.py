import pyqtgraph as pg
import numpy as np

class stringAxis(pg.AxisItem):
    def __init__(self, xdict, *args, **kwargs):
        pg.AxisItem.__init__(self, *args, **kwargs)
        self.x_values = np.asarray(list(xdict.keys()))
        self.x_strings = list(xdict.values())

    def tickStrings(self, values, scale, spacing):

        strings = []
        for v in values:
            vs = v * scale
            if vs in self.x_values:
                vstr = self.x_strings[np.abs(self.x_values-vs).argmin()]
            else:
                vstr = ""
            strings.append(vstr)

        return strings
