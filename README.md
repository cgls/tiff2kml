# TIFF2KML
Embeds GeoTIFF files in KML for display in Google Earth/Maps

Sample Python script that builds a ground overlay in Keyhole Markup Language (KML) format,
commonly used to display in Google Earth.

It currently takes a Quicklook (browse image in GeoTIFF format) 
as input and retrieves its coordinates using the open source GDAL library
before writing out the KML file.

Example:
python TIFF2KML.py g2_BIOPAR_FCOVER_QL_201207030000_OCEA_VGT_V1.3.tiff g2_BIOPAR_FCOVER_QL_201207030000_OCEA_VGT_V1.3.kml

To repeat for several quicklook files in same folder:
in Windows, Command Prompt
   for %I in (*_QL_*) do python QLtoKMLoverlay.py %I %~nI.kml
in Linux, bash shell
   for I in *_QL_*; do python QLtoKMLoverlay.py ${I} ${I/.tiff/.kml}

Hint:
For distribution to colleagues, take the quicklook image (input) and KML output file and 
put them together in a zip file. Then rename the zip file, replacing .zip with .kmz
Google Earth can open the zipped file (.kmz) directly.

References:
- Google - KML tutorial and samples - Ground overalay:
    https://developers.google.com/kml/documentation/kml_tut#ground-overlays
- GDAL - data model - GeoTransform
    http://www.gdal.org/gdal_datamodel.html

Limitations:
- Quicklooks are typically at reduced resolution (sub-sampled).
  Similar code can be developed for the actual, full-resolution layers in the data files (HDF5, NetCDF, GeoTiff).
  HDF5 files do not contain standardized georeference information, hence the GetGeoTransform
  will not provide the coordinates. Other CGLS tools will show how to deal with HDF5 data files.
  
Alternatives:
- The use of XML editing libraries in Python, as well as Google's of OGC schema of the 
  standardized KML format can help to update the tool in case the KML format is changed.
  This example is kept simple and shows the KML file's contents more explicitly.
  http://schemas.opengis.net/kml/
- GDAL utilities such as gdal_translate can convert geospatial data files to KMLSUPEROVERLAY format.
  See http://www.gdal.org/formats_list.html and http://www.gdal.org/gdal_translate.html
