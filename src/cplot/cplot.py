from CoolProp.CoolProp import PropsSI
import matplotlib.pyplot as plt
import numpy as np

class Cplot:
    def __init__(self, points, fluid) -> None:
        self.points = points
        self.fluid = fluid
        self.temp_precision = 0.1
    def saturation_line_t_s(self):
        Tmin = PropsSI('Tmin', fluido2)
        Tmax = PropsSI('TCRIT', fluido2)
        self.temp_range = np.arange(Tmin, Tmax, self.temp_precision)
        line_left = np.empty(0)
        line_right = np.empty(0)
        for i in temp:
          aux1 = PropsSI('S', 'T', i, 'Q',0, fluido2)
          line_left = np.append(line_left, float(aux1))
          aux2 = PropsSI('S', 'T', i, 'Q',1, fluido2)
          line_right = np.append(line_right, float(aux2))
        self.saturation_line_t_s = np.concatenate((line_left, line_right))
    def point_analysis(self):
        for point in self.points:
            if

    def plot_diagram_ts(self):
        # saturation line
        plt.plot(self.saturation_line_t_s, self.temp_range, color ="black")
        for i in self.points:
            plt.plot(i['s'], self.temp_range, marker='x', label=i["item"])
