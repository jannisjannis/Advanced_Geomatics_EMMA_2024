from pyqgis_scripting_ext.core import *

txtPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/stations.txt"

with open (txtPath,"r") as file:
    next(file)
    lines = file.readlines()
    
points = []
countrys = {}

for counter, line in enumerate(lines):
    linestrip = line.strip().split(',')
    lat = linestrip[3]
    lon = linestrip[4]
    country = linestrip[2]
    
    lat_split = lat.strip().split(':')
    lat_dd = float(lat_split[0])
    lat_min = float(lat_split[1])
    lat_ss = float(lat_split[2])
    lat_new = (lat_dd + (lat_min / 60) + (lat_ss / 3600))
    
    lon_split = lon.strip().split(':')
    lon_dd = float(lon_split[0])
    lon_min = float(lon_split[1])
    lon_ss = float(lon_split[2])
    lon_new = (lon_dd + (lon_min / 60) + (lon_ss / 3600))

    point = HPoint(lon_new, lat_new)
    points.append(point)

    count = countrys.get(country,0)
    count += 1
    countrys[country] = count

for country, counter in countrys.items():
    print(f"{country}: {counter}.")
    
canvas = HMapCanvas.new()

for point in points:
    canvas.add_geometry(point, "magenta", 1)

canvas.set_extent([0,-30,90,180])
canvas.show()