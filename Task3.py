# Import necessary modules
import arcpy
import os

# Check ArcPy product edition
arcpy.CheckProduct("ArcInfo")

# Set workspace
arcpy.env.workspace = "V:\ENV859_PS4\Data"
arcpy.env.overwriteOutput = True

# Create a list of all feature classes that start with "BMR"
bmr_feature_classes = arcpy.ListFeatureClasses("BMR_*")

# Import the tri-counties feature class
tri_counties = "TriCounties.shp"

# Loop through BMR features classes and split using tri-counties feature class
for bmr_class in bmr_feature_classes:
    # Extract BMR rank and remove the last 4 characters 
    bmr_rank = bmr_class.split("R")[1][:-4] #
    # Set the scratch folder path where output folders will be created
    out_folder_path = "V:\ENV859_PS4\Scratch"
    out_name = f"BMR{bmr_rank}"
    # Create output folders
    output_folder = arcpy.CreateFolder_management(out_folder_path, out_name)
    # Split the features in BMR by county features in tri_counties
    arcpy.analysis.Split(bmr_class, tri_counties, "CO_NAME", output_folder)
