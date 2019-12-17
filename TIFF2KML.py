#!/usr/bin/python
## @author Tim Jacobs, VITO NV, Belgium

import sys

#gdal library to help find out the coordinates
from osgeo import gdal

#for unicode (UTF-8) reading/writing in Python 2.x
import codecs

if len(sys.argv)<2:
    print "Usage", sys.argv[0], "input_ql_image_filename output_kml_filename"
    sys.exit(1)

ql_image_filename=sys.argv[1]
kml_output_filename=sys.argv[2]

overlay_name="My first KML overlay"

f=gdal.Open(ql_image_filename)
gt=f.GetGeoTransform()
east_longitude=gt[0]
west_longitude=east_longitude+(f.RasterXSize*gt[1])
north_latitude=gt[3]
#assumes first line is northern-most, GeoTransform[5] is negative
south_latitude=north_latitude+(f.RasterYSize*gt[5])

#sample content of KML file, with a few values to substitute
kml = (
'<?xml version="1.0" encoding="UTF-8"?>\n'
'<kml xmlns="http://www.opengis.net/kml/2.2">\n'
'  <Folder>\n'
'    <name>Ground Overlays</name>\n'
'    <description>Examples of ground overlays</description>\n'
'    <GroundOverlay>\n'
'      <name>%s</name>\n'
'      <Icon>\n'
'        <href>%s</href>\n'
'      </Icon>\n'
'      <LatLonBox>\n'
'        <north>%f</north>\n'
'        <south>%f</south>\n'
'        <east>%f</east>\n'
'        <west>%f</west>\n'
'      </LatLonBox>\n'
'    </GroundOverlay>\n'
'  </Folder>\n'
'</kml>\n'
   ) %(overlay_name, ql_image_filename, north_latitude, south_latitude, east_longitude, west_longitude)

with codecs.open(kml_output_filename, encoding='utf-8', mode='w+') as kmlFile:
    kmlFile.write(kml.encode('utf-8'))

#For web services: use following content-type header
#Content-Type: application/vnd.google-earth.kml+xml'
