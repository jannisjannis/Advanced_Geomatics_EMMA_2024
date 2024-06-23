from pyqgis_scripting_ext.core import *

csvPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/classes/Excersises/02_exe0_geometries.csv"

with open(csvPath,"r") as file:
    lines = file.readlines()
    
coordss = []
coordspolygon1 = []
coordspolygon2 = []
coordspoint = []
canvas = HMapCanvas.new()

for line in lines:
    line = line.strip().split(';')
    if line[0] == "line":
        coords = line[1].split(' ')
        for coord in coords:
            coord_list = coord.split(',')
            coords = [float(coord) for coord in coord_list]
            coordss.append(coords)
        line = HLineString.fromCoords(coordss)
        canvas.add_geometry(line, "red", 2)
    elif line[0] == "polygon":
        coords = line[1].split(' ')
        if line[2] == "1":
            for coord in coords:
                coord_list = coord.split(',')
                coords = [float(coord) for coord in coord_list]
                coordspolygon1.append(coords)
            polygon1 = HPolygon.fromCoords(coordspolygon1)
            canvas.add_geometry(polygon1, "blue", 2)
        elif line[2] == "2":
            for coord in coords:
                coord_list = coord.split(',')
                coords = [float(coord) for coord in coord_list]
                coordspolygon2.append(coords)
            polygon2 = HPolygon.fromCoords(coordspolygon2)
            canvas.add_geometry(polygon2, "green", 2)
    elif line[0] == "point":
        coord_list = line[1].split(',')
        coords = [float(coord) for coord in coord_list]
        coordspoint.append(coords)
        point = HMultiPoint.fromCoords(coordspoint)
        canvas.add_geometry(point, "black", 10)
    

canvas.set_extent([0,0,60,60])
canvas.show()
    