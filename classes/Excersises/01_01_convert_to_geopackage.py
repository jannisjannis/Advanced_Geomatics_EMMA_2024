from pyqgis_scripting_ext.core import *

txtPath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Introduction/stations.txt"
folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/Processingvectordata_excersise/"

fields = {
    "id": "Integer",
    "name": "String",
    "country": "String",
    "elevation": "Integer"
}

stationslayer = HVectorLayer.new("stations", "Point", "EPSG:3857", fields)
crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

with open(txtPath,"r") as file:
    next(file)
    lines = file.readlines()
    
    for line in lines:
        splitline = line.strip().split(",")
        
        ID = splitline[0].strip()
        NAME = splitline[1].strip()
        COUNTRY = splitline[2].strip()
        
        latsplit = splitline[3].strip().split(":")
        lathour = float(latsplit[0])
        latminute = float(latsplit[1])
        latsecond = float(latsplit[2])
        LAT = lathour + latminute/60 + latsecond/3600
        
        lonsplit = splitline[4].strip().split(":")
        lonhour = float(lonsplit[0])
        lonminute = float(lonsplit[1])
        lonsecond = float(lonsplit[2])
        LON = lonhour + lonminute/60 + lonsecond/3600
        
        Point = HPoint(LON, LAT)
        POINT = crsHelper.transform(Point)
        # POINT = HPoint (LON, LAT)
        ELEVATION = float(splitline[5].strip())
        
        stationslayer.add_feature(POINT, [ID, NAME, COUNTRY, ELEVATION])

path = folder + "stations.gpkg"
hopenotError = stationslayer.dump_to_gpkg(path, overwrite = True)
if hopenotError:
    print(hopenotError)
        