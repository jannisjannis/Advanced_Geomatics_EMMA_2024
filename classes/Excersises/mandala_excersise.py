from math import cos, sin, radians
from pyqgis_scripting_ext.core import *

point_list = []
n = 3
d = 2
iterations = 20
maxAngle = 360*iterations


#define an angle
for angle in range(0, maxAngle, 1):
    radAngle = radians(angle)
    k = n/d
    r = cos(k*radAngle)
    x = r*cos(radAngle)
    y = r*sin(radAngle)
    point = ([x,y])
    point_list.append(point)
    
canvas = HMapCanvas.new()
line = HLineString.fromCoords(point_list)
canvas.add_geometry(line, "blue", 2)
canvas.set_extent(line.bbox())
canvas.show()


# for point in point_list:
#     print(point)