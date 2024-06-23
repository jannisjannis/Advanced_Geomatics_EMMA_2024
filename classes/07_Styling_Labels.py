from pyqgis_scripting_ext.core import *


folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"
tmpFolder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/temp"
geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"
citiesName = "ne_50m_populated_places"
riversName = "ne_10m_rivers_lake_centerlines_scale_rank"

#cleanup first -> remove old layers
HMap.remove_layers_by_name(["OpenStreetMap", countriesName, citiesName, "rivers_italy"]) #makes it that you dont end up with hundreds of OpenStreetMap Layers

#load openstreetmap tiles layer
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#load the citieslayer
citiesLayer = HVectorLayer.open(geopackagePath, citiesName)

citiesLayer.subset_filter("SOV0NAME = 'Italy'")

pointStyle = HMarker("square", 6, 45) + \
                HFill("red") + HStroke("black, 1") 

field = "NAME"
pointStyle += HLabel(field, yoffset = -8) + HHalo("white", 1)
field = "if(POP_MAX > 1000000, concat(NAME, '(',round(POP_MAX/1000000, 1),')'), NAME)"  #last part, if not just put the name


labelProperties = {
    "font": "Arial",
    "color": "black",
    "size": 10,
    "field": field,
    "xoffset": 0,
    "yoffset": -8
}
pointStyle += HLabel(**labelProperties) + HHalo("white", 2)

citiesLayer.set_style(pointStyle)

#polygon layer
countriesLayer = HVectorLayer.open(geopackagePath, countriesName)
countriesLayer.subset_filter("NAME = 'Italy'")
italyGeometry = countriesLayer.features()[0].geometry

print(italyGeometry.centroid())

polygonStyle = HFill("0,255,0,128") + HStroke("green, 2") #128 means how much transparency, first numbers mean rgb
countriesLayer.set_style(polygonStyle)

#lines layer
riversLayer = HVectorLayer.open(geopackagePath, riversName)
riversLayerItaly = riversLayer.sub_layer(italyGeometry, "rivers_italy", ['scalerank', 'name'])

#thematic styling
ranges = [
    [0,0],
    [1,5],
    [6,7],
    [8,9],
    [10,11]
]
styles = [
    HStroke("blue",7),
    HStroke("blue",5),
    HStroke("blue",3),
    HStroke("blue",2),
    HStroke("blue",1)
]

labelProperties = {
    "font": "Arial",
    "color": "blue",
    "size": 14,
    "field": 'name',
    "along_line": True, #where possible and readible along the line
    "bold": True,
    "italic": True
}
labelStyle = HLabel(**labelProperties) + HHalo("white", 1)
riversLayerItaly.set_graduated_style('scalerank', ranges, styles, labelStyle)

# riversStyle = HStroke("blue", 2)
# riversStyle += labelStyle
# riversLayerItaly.set_style(riversStyle + labelStyle)

HMap.add_layer(countriesLayer)
HMap.add_layer(riversLayerItaly)
HMap.add_layer(citiesLayer)

printer = HPrinter(iface)

mapProperties = {
    "x": 5,
    "y": 25,
    "width": 285,
    "height": 180,
    "extent": countriesLayer.bbox(), #[10, 44, 12, 46],
    "frame": True
}

printer.add_map(**mapProperties)

labelProperties = {
    "x": 120,
    "y": 10,
    "text": "Such a nice map",
    "font_size": 28,
    "bold": True,
    "italic": False
}
printer.add_label(**labelProperties)

legendProperties = {
    "x": 215,
    "y": 30,
    "width": 150,
    "height": 100,
    "max_symbol_size": 3
}
printer.add_legend(**legendProperties)

scalebarProperties = {
    "x": 10,
    "y": 190,
    "units": "km",
    "segments": 4,
    "unit_per_segment": 10,
    "style": "Single Box",
    "font_size": 12
}
printer.add_scalebar(**scalebarProperties)
#import datetime
#print(datetime.datetime.now())  "YYYY-MM-DD HH:MM:SS"

outputPdf = f"{tmpFolder}/test.pdf"
printer.dump_to_pdf(outputPdf)

outputPng = f"{tmpFolder}/test.png"
printer.dump_to_image(outputPng)


