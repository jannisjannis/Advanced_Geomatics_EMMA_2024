from pyqgis_scripting_ext.core import *

polygons = []
i = 6
startingpolygon = [[0,-84],[0,84],[6,84],[6,-84],[0,-84]]

for x in range(60):
    polygon = []
    for coords in startingpolygon:
        lat = coords[0]
        lon = coords[1]
        lat = float(lat)
        lon = float(lon)
        lat_new = lat + i*x
        coords_new = (lat_new, lon)
        polygon.append(coords_new)
    poly_new = HPolygon.fromCoords(polygon)
    polygons.append(poly_new)

canvas = HMapCanvas.new()

for polygon in polygons:
    canvas.add_geometry(polygon, "magenta", 2)

canvas.set_extent([-10,-90,370,90])
canvas.show()
    
    
