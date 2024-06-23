from pyqgis_scripting_ext.core import*

folder = "C:/Users/Jannis/OneDrive - Scientific Network South Tyrol/Documents/Master - EMMA/2.Semester/Advanced Geomatics/"

geopackagePath = folder + "natural_earth_vector.gpkg/packages/natural_earth_vector.gpkg"
countriesName = "ne_50m_admin_0_countries"

countriesLayer = HVectorLayer.open(geopackagePath, countriesName)

ranges = [
    [80000000, float('inf')],
    [1000000, 80000000],
    [float('-inf'), 1000000],
]

styles = [
    HFill("217, 0, 0, 128"),
    HFill("0, 255, 0, 128"),
    HFill("0, 0, 255, 128"),
]

labelStyle = HLabel("POP_EST") + HHalo()
countriesLayer.set_graduated_style("POP_EST", ranges, styles, labelStyle)
HMap.add_layer(countriesLayer)