# Import necessary modules
import sys
import arcpy

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
arcpy.env.overwriteOutput = True

# Define the path to the input Streams.shp feature class (file name only)
inputFile = "Streams.shp"

# Define a list of buffer distances
buffer_distances = [100, 200, 300, 400, 500]

# Create a for loop, that iterates through each buffer distance and exports it to an appropriately named output
for dist in buffer_distances:
    buffer_dist_2 = f"{dist} meters"
    out_feature_class = out_feature_class = f"V:\\ENV859_PS4\\Scratch\\buff_{dist}m.shp" 

    # Execute the buffer command

    arcpy.Buffer_analysis(inputFile, out_feature_class, buffer_dist_2,"FULL","ROUND", "ALL")

# Display any warnings or errors
print(arcpy.GetMessages())
