# Import necessary modules
import sys
import arcpy

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
arcpy.env.overwriteOutput = True

# Define the path to the input Streams.shp feature class (file name only)
inputFile = "Streams.shp"

# Get user input for buffer distance and output file path
buffer_dist = arcpy.GetParameterAsText(0)  # e.g., "1000"
buffer_dist_2 = f"{buffer_dist} meters"
out_feature_class = f"V:\\ENV859_PS4\\Scratch\\buff_{buffer_dist}m.shp" 

# Execute the buffer command

arcpy.Buffer_analysis(inputFile, out_feature_class, buffer_dist_2,"FULL","ROUND", "ALL")

# Display any warnings or errors
print(arcpy.GetMessages())
