#Excersise 2 - cities inside france 

from pyqgis_scripting_ext.core import *

#cleanup first -> remove old layers
HMap.remove_layers_by_name(["OpenStreetMap"]) #makes it that you dont end up with hundreds of OpenStreetMap Layers

folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"
geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"


#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)

#this is all about the country France
# print("Schema (first 4 fields):")
# counter = 0
# for name, type in countriesLayer.fields.items():
#     counter += 1
#     if counter < 10:
#         print("\t", name, "of type", type)

crs = countriesLayer.prjcode
# print("Projection: ", crs)
# print("Spatial extent:", countriesLayer.bbox())
# print("Feature count:", countriesLayer.size())

# print("Attributes for France:")
nameIndex = countriesLayer.field_index("NAME") #care about the spelling
countriesFeatures = countriesLayer.features()

for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "Germany":
        geometry = feature.geometry
        print("Geom:", geometry.asWkt()[:50] + "...")
        
        
#this is all about the cities now
# print("Schema (first 4 fields):")
# counter = 0
# for name, type in citiesLayer.fields.items():
#     counter += 1
#     if counter < 10:
#         print("\t", name, "of type", type)

crs = citiesLayer.prjcode
# print("Projection: ", crs)
# print("Spatial extent:", citiesLayer.bbox())
# print("Feature count:", citiesLayer.size())

# print("Attributes for Cities:")
nameIndex = citiesLayer.field_index("NAME") #care about the spelling
latIndex = citiesLayer.field_index("LATITUDE")
lonIndex = citiesLayer.field_index("LONGITUDE")
citiesFeatures = citiesLayer.features()

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

canvas = HMapCanvas.new()
canvas.set_layers([osm])
geometry_trans = crsHelper.transform(geometry)

for feature in citiesFeatures:
    name = feature.attributes[nameIndex]
    lat = feature.attributes[latIndex]
    lat = float(lat)
    lon = feature.attributes[lonIndex]
    lon = float(lon)
    point = HPoint(lon,lat)
    point_trans = crsHelper.transform(point)
    canvas.add_geometry(point_trans, "blue",2)
    if geometry_trans.contains(point_trans):
        print(name)
        
        
canvas.add_geometry(geometry_trans, "red", 2)

canvas.set_extent(geometry_trans.bbox())
canvas.show()
    