from pyqgis_scripting_ext.core import*

folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"

geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"

schema = {
    "name": "string"
}

centroidsLayer = HVectorLayer.new("centroids", "Point", "EPSG:4326", schema)

countryLayer = HVectorLayer.open(geopackagePath, countriesName)

notInCountryList = []
nameIndex = countryLayer.field_index("NAME")
for country in countryLayer.features():
    countryGeom = country.geometry
    name = country.attributes[nameIndex]
    
    centroid = countryGeom.centroid()
    
    centroidsLayer.add_feature(centroid,[name])
    
    if not centroid.intersects(countryGeom):
        notInCountryList.append(name)
    
simpleStyle = HMarker("circle", 10) + HLabel("name") + HHalo()
centroidsLayer.set_style(simpleStyle)
HMap.add_layer(centroidsLayer)
print("Countries with Centroids not inside the main polygon:")

for c in notInCountryList:
    print(c)

