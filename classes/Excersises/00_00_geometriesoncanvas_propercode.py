from pyqgis_scripting_ext.core import *

csvPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/classes/Excersises/02_exe0_geometries.csv"

points = []
lines_list = []
polygons = []

with open(csvPath,"r") as file:
    lines = file.readlines()
    
    for line in lines:
        linestrip = line.strip().split(';')
        
        geometry = linestrip[0]
        coords = linestrip[1]
        number = linestrip[2]
        
        if geometry == "point":
            coordsplit = coords.split(',')
            lat = coordsplit[0]
            lon = coordsplit[1]
            lat = float(lat)
            lon = float(lon)
            point = HPoint(lat,lon)
            points.append(point)
            
        elif geometry == "line":
            coordssplit = coords.split(' ')
            coordslist = []
            for coords in coordssplit:
                coordssplitted = coords.split(',')
                lat = coordssplitted[0]
                lon = coordssplitted[1]
                lat = float(lat)
                lon = float(lon)
                point = (lat,lon)
                coordslist.append(point)
            coordslista = HLineString.fromCoords(coordslist)
            lines_list.append(coordslista)
        
        elif geometry == "polygon":
            coordssplit = coords.split(' ')
            coordslist = []
            for coords in coordssplit:
                coordssplitted = coords.split(',')
                lat = coordssplitted[0]
                lon = coordssplitted[1]
                lat = float(lat)
                lon = float(lon)
                point = (lat,lon)
                coordslist.append(point)
            coordslista = HPolygon.fromCoords(coordslist)
            polygons.append(coordslista)
        

canvas = HMapCanvas.new()

for point in points:
    canvas.add_geometry(point, "blue", 7)

for line in lines_list:
    canvas.add_geometry(line, "red", 2)

for polygon in polygons:
    canvas.add_geometry(polygon, "green", 2)
    
    
canvas.set_extent([0,0,60,60])
canvas.show()
    