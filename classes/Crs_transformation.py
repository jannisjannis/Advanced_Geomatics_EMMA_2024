from pyqgis_scripting_ext.core import *

crsHelper = HCrs()
crsHelper.from_srid(4326)   #thats the orginal datum of QGIS
crsHelper.to_srid(32632)

point4326 = HPoint(11,46)
point32632 = crsHelper.transform(point4326)

# print(f"{point4326} -> {point32632}")

# backto4326 = crsHelper.transform(point32632, inverse = True)
# print(backto4326)