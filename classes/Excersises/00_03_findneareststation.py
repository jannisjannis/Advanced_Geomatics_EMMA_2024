from pyqgis_scripting_ext.core import *

lat_input = 46.49809

lon_input = 11.34999


point_input = HPoint(lat_input, lon_input)

txtPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/stations.txt"

with open (txtPath,"r") as file:
    next(file)
    lines = file.readlines()
    
stations = []

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
    
    point = HPoint(lat_new, lon_new)
    distance = point_input.distance(point)
    station_data = [station, point, distance]
    stations.append(station_data)

minDistance = 9999
nearestStationName = "none"
nearestDistancePoint = None


for station_data in stations:
    station = station_data[0]
    distance = station_data[2]
    
    if distance < minDistance:
        minDistance = distance
        nearestStationName = station
        nearestDistancePoint = point

# min_distance_index = min(range(len(stations)), key=lambda i: stations[i][2])
# nearest_station_data = stations[min_distance_index]
# nearest_station_name = nearest_station_data[0]
# nearest_station_coordinates = nearest_station_data[1]
# nearest_station_distance = nearest_station_data[2]

# print(f"")
# print("The nearest station is:", nearest_station_name.strip())
# print("Coordinates:", nearest_station_coordinates)
# print("Distance:", nearest_station_distance)

print(f"")
print("The nearest station is:", nearestStationName.strip())
print("Coordinates:", nearestDistancePoint)