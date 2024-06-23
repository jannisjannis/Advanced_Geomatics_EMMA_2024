from pyqgis_scripting_ext.core import *

point = HPoint(30.0, 10.0)     #always long, lat (x and then y)
print(point.asWkt())     #asWellknowntext

coords = [[31, 11], [10,30], [20,40], [40,40]]
line = HLineString.fromCoords(coords)  #Coords is a function he wrote
print(line.asWkt())   #could also only print line here

coords = [[32,12], [10,20], [20, 39], [40,39], [32,12]]
polygon = HPolygon.fromCoords(coords)
print(polygon)  #polygons could have holes -> not this one

exteriorPoints = [[35,10], [10,20], [15,40], [45,45], [35,10]]
holePoints = [[20,30], [35,35], [30,20], [20,30]]
polygonWithHole = HPolygon.fromCoords(exteriorPoints)

holeRing = HLineString.fromCoords(holePoints)
polygonWithHole.add_interior_ring(holeRing)

print(polygonWithHole)

#multis
coords = [[10,40], [40,30], [20,20], [30,10]] #doesnt show all the points because they are under the line
multiPoints = HMultiPoint.fromCoords(coords)
print(multiPoints)

coords1 = [[10,10],[20,20],[10,40]]
coords2 = [[40,40], [30,30], [40,20], [30,10]]
multiLine = HMultiLineString.fromCoords([coords1,coords2])

coords1 = [[30,20], [10,40], [45,40], [30,20]]
coords2 = [[15,5], [40,10], [10,20], [5,10], [15,5]]

multiPolygon = HMultiPolygon.fromCoords([coords1,coords2])

subGeometries = multiPolygon.geometries() #returns geometrys of objects
colors = [("green"), ("red")]

coordinates = polygon.coordinates()
for coord in coordinates:
    print(f" coord x = {coord[0]} / coord y = {coord[1]}")
    
wkt = "POINT (156 404)"
pointGeom = HGeometry.fromWkt(wkt)
print(pointGeom)

wkt = """
MULTIPOLYGON (((130 510, 140 450, 200 480, 210 570, 150 630, 130 560, 130 510)),
((430 770, 370 820, 210 860, 20 760, 35 631, 100 370, 108 363, 154 284, 230 380,
140 400, 150 440, 130 450, 104 585, 410 670, 440 590, 450 590, 430 770)))
"""
polygonGeom = HGeometry.fromWkt(wkt)

canvas = HMapCanvas.new() #add a canvas -> empty map
canvas.add_geometry(polygonGeom, "red", 2)
# for i, geometry in enumerate(subGeometries):
#     canvas.add_geometry(subGeometries[i],colors[i], 2)
    
#or
# for index in range(len(subGeometries)):
#     geom = subGeometries[index]
#     color = colors[index]
#     canvas.add_geometry(geom, color, 2)


# canvas.add_geometry(point, "red", 2)   #(show what, color,thickness)
# canvas.add_geometry(multiPolygon, "yellow", 5)
# canvas.add_geometry(multiLine, "blue", 5)
# canvas.add_geometry(multiPoints, "red", 15)
# canvas.add_geometry(line, "blue", 2)
# canvas.add_geometry(polygon, "green", 2)
# canvas.add_geometry(polygonWithHole, "magenta", 2)
# # -> we didnt say where it needs to show that
canvas.set_extent([0,0,1000,1000])   #([xmin, ymin, xmax, ymax)
canvas.show()