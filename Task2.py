# Import necessary modules
import sys
import arcpy

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
arcpy.env.overwriteOutput = True

# Define the path to the input Streams.shp feature class (file name only)
inputFile = "Roads.shp"

# Create road type class string variable
roadType = "0;201;203"

# Create a list variable 
value_list = roadType.split(";")

# Loop through each road type value

for road_type in value_list:
    # Define the output feature class path with road type in the name
    out_feature_class = f"V:\\ENV859_PS4\\Scratch\\roads_{road_type}.shp"
    
    # Define where clause
    where_clause = f"ROAD_TYPE = {road_type}"

    # Execute Select
    arcpy.Select_analysis(inputFile, out_feature_class, where_clause)

