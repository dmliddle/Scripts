# Import modules
import sys, os, arcpy

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
# Set variables
inputFile = 'V:\ENV859_PS4\Data\Streams.shp'
out_feature_class = 'V:\ENV859_PS4\Scratch\StrmBuff1km.shp'
# Set output variable

# Second string variable that sets distance to 1000 meters
buff_dist = "1000 meters"



