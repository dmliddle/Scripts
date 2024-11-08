# Import necessary modules
import sys
import os
import arcpy

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"

# Allow overwriting of outputs
arcpy.env.overwriteOutput = True

# Define the path to the input Streams.shp feature class
inputFile = 'Streams.shp'

# Define the buffer distance as "1000 meters"
buff_dist = "1000 meters"

# Define the path and filename for the output buffer feature class in the Scratch folder
out_feature_class = 'V:\ENV859_PS4\Scratch\StrmBuff1km.shp'

# Execute the buffer command

arcpy.Buffer_analysis(inputFile, out_feature_class, buff_dist,"FULL","ROUND", "ALL")

# Display any warnings or errors
print(arcpy.GetMessages())
