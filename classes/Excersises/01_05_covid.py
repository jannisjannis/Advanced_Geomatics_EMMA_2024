from pyqgis_scripting_ext.core import *


folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"
geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
provincesName = "ne_10m_admin_1_states_provinces"

dataPath = f"{folder}/classes/Excersises/dpc-covid19-ita-regioni.csv"

outputFolder = f"{folder}/temp/output/"

HMap.remove_layers_by_name([provincesName, "OpenStreetMap"])

#add osm
osm = HMap.get_osm_layer()
HMap.add_layer(osm)

#add layer
provincesLayer = HVectorLayer.open(geopackagePath, provincesName)
HMap.add_layer(provincesLayer)

#add subste filter to layer
provincesLayer.subset_filter("iso_a2='IT'")
#get provinces and merge them to regions
#creat dict containing region name and its geometry

regionName2GeometryMap = {}
regionIndex = provincesLayer.field_index("region") #looking for index of region column
for provinceFeature in provincesLayer.features():
    geometry = provinceFeature.geometry
    regionName = provinceFeature.attributes[regionIndex]
        
    regionGeometry = regionName2GeometryMap.get(regionName) #get region geometry for the looped regionName, as still empty it will give you none
    if regionGeometry != None: #if there is a geometry  do union it
        regionGeometry = regionGeometry.union(geometry)#pass will ignore, continue would jump up to the for loop and dont do the else
    else: #if there isnt a geometry, use regionGeometry
        regionGeometry = geometry
    regionName2GeometryMap[regionName] = regionGeometry

with open(dataPath, 'r') as file:
    lines = file.readlines()

day2featuresMap = {}
for index, line in enumerate(lines):
    lines = line.strip()
    
    if index < 500:
        lineSplit = line.split(",")
        # 0 -> date
        #3 -> region
        #17 -> total cases
        #4,5 -> lat, long
        dayAndTime = lineSplit[0]
        dayAndTime = dayAndTime.split("T")
        day = dayAndTime[0]
        
        if day.endswith("01"):
            region = lineSplit[3]
            totalCases = int(lineSplit[17])
            
            lat = float(lineSplit[4])
            lon = float(lineSplit[5])
            dataPoint = HPoint(lon,lat)
            
            for regionName, regionGeometry in regionName2GeometryMap.items():
                if regionGeometry.intersects(dataPoint):
                    featuresList = day2featuresMap.get(day)
                    if featuresList:
                        featuresList.append((regionGeometry, [day, region, totalCases]))
                    else:
                        featuresList = [(regionGeometry, [day, region, totalCases])]
                    day2featuresMap[day] = featuresList

imagePathsList = []
for day, featuresList in day2featuresMap.items():
    #if day != "2020-04-01":
        #continue
    
    print("Generating day", day)
    newLayerName = "covid_italy"
    HMap.remove_layer_by_name(newLayerName)
    
    schema = {
        "day": "string",
        "region": "string",
        "totcases": "int"
        }
        
    covidLayer = HVectorLayer.new(newLayerName, "Multipolygon", "EPSG:4326", schema)
    
    
for geometry, attributes in featuresList:
    covidLayer.add_feature(geometry, attributes)
        
    #style = HFill('yellow') + HStroke('black', 0.5)
    #covidLayer.set_style(style)
        
        
            
    ranges = [
        [float('-inf'), 1000],
        [1001, 3000],
        [3001, 10000],
        [10001, 40000],
        [40001, 100000],
        [100001, float('inf')]
    ]
    
    styles = [
        HFill('yellow') + HStroke('white', 0.5),
        HFill('green') + HStroke('white', 0.5),
        HFill('blue') + HStroke('white', 0.5),
        HFill('orange') + HStroke('white', 0.5),
        HFill('red') + HStroke('white', 0.5),
        HFill('black') + HStroke('white', 0.5),
    ]
    
    labelStyle = HLabel('totcases', size = 8, color = 'black') + HHalo() + HFill()
    covidLayer.set_graduated_style("totcases", ranges, styles, labelStyle)
    
    HMap.add_layer(covidLayer)
    
    printer = HPrinter(iface)
    mapProperties = {
        "x": 5,
        "y": 25,
        "width": 285,
        "height": 180,
        "frame": True,
        "extent": provincesLayer.bbox()
    }
    printer.add_map(**mapProperties)
    
    legendProperties = {
        "x": 210,
        "y": 30,
        "width": 150,
        "height": 100,
        "frame": True
    }
    printer.add_legend(**legendProperties)
    
    labelProperties = {
        "x": 120,
        "y": 10,
        "text": "COVID Italy, total Cases",
        "bold": True,
    }
    printer.add_label(**labelProperties)
    
    labelProperties = {
        "x": 30,
        "y": 190,
        "text": day,
        "font_size": 28,
        "bold": True
    }
    printer.add_label(**labelProperties)
    
    imageName = f"{day}_covid.png"
    imagePath = f"{outputFolder}/{imageName}"
    printer.dump_to_image(imagePath)
    imagePathsList.append(imagePath)

#generate the final animation
from PIL import Image

imagesList = []
for path in imagePathsList:
    img = Image.open(path)
    imagesList.append(img)

animationPath = f"{outputFolder}/covid_animation.gif"

imagesList[0].save(animationPath, save_all = True, append_images = imagesList[1:], duration = 500)

for path in imagePathsList:
    os.remove(path)

