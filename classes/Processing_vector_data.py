from pyqgis_scripting_ext.core import *

folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"
geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
testName = "test"

#cleanup first -> remove old layers
HMap.remove_layers_by_name(["OpenStreetMap", "test", citiesName]) #makes it that you dont end up with hundreds of OpenStreetMap Layers

#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#load the countries layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

print("Schema (first 4 fields):")

counter = 0
for name, type in countriesLayer.fields.items():
    counter += 1
    if counter < 5:
        print("\t", name, "of type", type)

crs = countriesLayer.prjcode
print("Projection: ", crs)
print("Spatial extent:", countriesLayer.bbox())
print("Feature count:", countriesLayer.size())

print("Attributes for Italy:")
nameIndex = countriesLayer.field_index("NAME") #care about the spelling
countriesFeatures = countriesLayer.features()
for feature in countriesFeatures:
    name = feature.attributes[nameIndex]
    if name == "Italy":
        geometry = feature.geometry
        print("Geom:", geometry.asWkt()[:50] + "...")

expressions = "NAME like'I%' AND POP_EST > 3000000"   #starts with the letter I
filteredCountriesFeatures = countriesLayer.features(expressions)
count = 0

for feature in filteredCountriesFeatures:
    print(feature.attributes[nameIndex])
    count += 1
print("Feature count with filter", count)

lon = 11.119982
lat = 46.080428
point = HPoint(lon, lat)
buffer = point.buffer(2)    #this means 2°

citiesLayer = HVectorLayer.open(geopackagePath, citiesName)
HMap.add_layer(citiesLayer)

citiesNameIndex = citiesLayer.field_index("NAME")
aoi = buffer.bbox()

count = 0
for feature in citiesLayer.features(bbox = aoi):
    print(feature.attributes[citiesNameIndex])
    count += 1
print("Cities features listed:", count)

count = 0   #set back count to zero
for feature in citiesLayer.features(geometryfilter = buffer):
    print(feature.attributes[citiesNameIndex])
    count += 1
print("Cities features listed with geometry filter:", count)


#create data


#create a schema
fields = {
    "id": "Integer",
    "name": "String"
}
just2citiesLayer = HVectorLayer.new("test", "Point", "EPSG:4326", fields)  #layer is namend test, creates point has the CRS and looks like fields
just2citiesLayer.add_feature(HPoint(-122.42, 37.78), [1, "San Francisco"])
just2citiesLayer.add_feature(HPoint(-73.98, 40.47), [1, "New York"])

path = folder + "test.gpkg"
hopenotError = just2citiesLayer.dump_to_gpkg(path, overwrite = True)
if hopenotError:
    print(hopenotError)

testLayer = HVectorLayer.open(path, testName)
HMap.add_layer(testLayer)

fields = {
    "name": "String",
    "population": "Integer",
    "lat": "Double",
    "lon": "Double"
}

oneCityMoreAttributes = HVectorLayer.new("test2", "Point", "EPSG:4326", fields)
oneCityMoreAttributes.add_feature(HPoint(-73.98, 40.47), \
                                        ["New York", 19040000, 40.47, -73.99])

hopeNotError = oneCityMoreAttributes.dump_to_gpkg(path, overwrite = False)
if hopeNotError:
    print(hopeNotError)
