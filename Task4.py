# Import necessary modules
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# User input variable
inFC = arcpy.GetParameterAsText(0)

# Describe a feature class using arcpy.da.Describe
desc = arcpy.da.Describe(inFC)

#Catalog path message
arcpy.AddMessage ("Catalog path: "+desc["catalogPath"])

# Extent message
extent = desc['extent']
arcpy.AddMessage(f"XMin: {round (extent.XMin,1)}")
arcpy.AddMessage(f"XMax: {round (extent.XMax,1)}")
arcpy.AddMessage(f"YMin: {round (extent.YMin,1)}")
arcpy.AddMessage(f"YMax: {round (extent.YMax,1)}")

# Check data set type  
if desc['datasetType'] == "FeatureClass":
    arcpy.AddWarning(desc['shapeType'])

elif desc['datasetType'] == "RasterDataset":
    arcpy.AddWarning(f"Raster Format: {desc['format']}")
    arcpy.AddWarning(f"# of Rows: {desc['height']}")
    arcpy.AddWarning(f"# of Columns: {desc['width']}")

else:
    arcpy.AddError(f"Data type not supported: {desc['datasetType']}")