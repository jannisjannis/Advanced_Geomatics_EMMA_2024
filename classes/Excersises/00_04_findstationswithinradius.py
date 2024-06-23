from pyqgis_scripting_ext.core import *

lat_input = 46.49809

lon_input = 11.34999

radius = 20000

stations = []
crsHelper = HCrs()
crsHelper.from_srid(4326)   #thats the orginal datum of QGIS
crsHelper.to_srid(32632)

point_inputt = HPoint(lon_input, lat_input)
point_input = crsHelper.transform(point_inputt)
buffer_input = point_input.buffer(radius)


txtPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/stations.txt"

with open (txtPath,"r") as file:
    next(file)
    lines = file.readlines()

for counter, line in enumerate(lines):
    linestrip = line.strip().split(',')
    lat = linestrip[3]
    lon = linestrip[4]
    station = linestrip[1]
    
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
    
    point4326 = HPoint(lon_new, lat_new)
    point32632 = crsHelper.transform(point4326)
   
    distance = round(point_input.distance(point32632), 1)
    station_data = [station, point32632, distance]
    stations.append(station_data)


for counter, station_data in enumerate(stations):
    station = station_data[0]
    POINT = station_data[1]
    distance = station_data[2]
    if POINT.intersects(buffer_input):
        print(f"")
        print("Stations within the buffer are:", station.strip())
        print("Coordinates:", POINT)
        print("Distance:", round(distance/1000,2), "km.")
        