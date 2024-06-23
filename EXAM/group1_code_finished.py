from pyqgis_scripting_ext.core import *

folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/EXAM/"
geopackagePath = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
path = folder + "locations.gpkg"

# import the http requests library to get stuff from the internet
import requests
# import the url parsing library to urlencode the query
import urllib.parse
# define the query to launch
endpointUrl = "https://query.wikidata.org/sparql?query=";
# define the query to launch
query = """SELECT ?place ?placeLabel ?placeDescription ?location ?elev ?image WHERE
{
    ?place p:P2044/psv:P2044 ?placeElev.
    ?place wdt:P17 wd:Q38.
    ?placeElev wikibase:quantityAmount ?elev.
    ?placeElev wikibase:quantityUnit ?unit.
    bind(0.01 as ?km).
    filter( (?elev < ?km*1000 && ?unit = wd:Q11573)
    || (?elev < ?km*3281 && ?unit = wd:Q3710)
    || (?elev < ?km && ?unit = wd:Q828224) ).
    ?place wdt:P625 ?location.
    optional { ?place wdt:P18 ?image }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en" }
} """

# URL encode the query string
encoded_query = urllib.parse.quote(query)
# prepare the final url
url = f"{endpointUrl}{encoded_query}&format=json"
# run the query online and get the produced result as a dictionary
r=requests.get(url)
result = r.json()
#print(result)

HMap.remove_layers_by_name(["OpenStreetMap", "ne_50m_admin_0_countries", "locations"])

osm = HMap.get_osm_layer()
HMap.add_layer(osm)

countriesName = "ne_50m_admin_0_countries"
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
HMap.add_layer(countriesLayer)
countriesLayer.subset_filter("ADMIN='Italy'")
#create a geopackage based on the result, both the georaphic and alphanumeric part

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)

#therefore first set the outline of the geopackage

fields = {
    "place": "String",
    "place_Label": "String",
    "elevation": "Integer"
}

#location not because this is saved as the point

entitiesLayer = HVectorLayer.new("locations", "Point", "EPSG:3857", fields)

for entity in result['results']['bindings']:
    place = entity['place']['value']
    place_Label = entity['placeLabel']['value']
    elevation = float(entity['elev']['value'])
    location = entity['location']['value']
    
    coordssplit = location.split(" ")
    lon = coordssplit[0][6:]
    lon = float(lon)
    
    lat = coordssplit[1][:-1]
    lat = float(lat)
    
    POINT = HPoint(lon, lat)
    Point = crsHelper.transform(POINT)
    
    if elevation > 10:
        entitiesLayer.add_feature(Point, [place, place_Label, elevation])
    
crsHelper = HCrs()
crsHelper.from_srid(4326)#open street map data (latlong)
crsHelper.to_srid(3857)#reference system for webmapping adapted to the all word

hopenotError = entitiesLayer.dump_to_gpkg(path, overwrite = True)
if hopenotError:
    print(hopenotError)

# # place_Description = location['placeDescription']['value']

# geopackagePath = folder + "locations.gpkg"
# Points_Italy = "locations"

# Countries border style

styles = HFill("Transparent") + HStroke("black", 0.5)
countriesLayer.set_style(styles)

# Locations style

styles1 = HMarker("point", 3) + HStroke("purple", 1) + HFill("purple")

labelProperties = {
    "font": "Arial",
    "color": "black",
    "size": 8,
    "field": 'place_Label',
    "xoffset": 0,
    "yoffset": -4,
    "along_line": True,
    "bold": True,
    "italic": False
}

styles1 += HLabel(**labelProperties) + HHalo("white", 1)

entitiesLayer.set_style(styles1)

# Add layers to the map

HMap.add_layer(entitiesLayer)
HMap.add_layer(countriesLayer)