# Import necessary modules
import arcpy
import os
import sys

arcpy.env.overwriteOutput = True

# Set workspace
arcpy.env.workspace = "V:/ENV859_PS4/Data"

# Get the input feature class and field name from the user
input_fc = arcpy.GetParameterAsText(0)  # Feature class
input_field = arcpy.GetParameterAsText(1)  # Field name to retrieve

# Create a point object at specified coordinates
point = arcpy.Point(590000, 230000)

# The cursor retrieves the Shape field and the user-specified field
with arcpy.da.SearchCursor(input_fc, ["SHAPE@", input_field]) as cursor:
    # Iterate through each feature
    for row in cursor:
        # Assign the Shape object of the current feature to recShape
        recShape = row[0]  # Shape@ field contains the geometry
        
        # Check if the point is within the current feature's shape
        if recShape.contains(point):
            # Get the attribute value of the specified field
            field_value = row[1]
            
            # Send a message back to ArcGIS Pro with the field value
            arcpy.AddMessage(f"The point intersects with {field_value} County.")
            break
    else:
        # If no intersection was found, send a message
        arcpy.AddMessage("No intersecting feature found for the specified point.")