import geopandas as gpd
from shapely.ops import unary_union
import shapely
import laspy
import glob
import os

print("-" * 50)
print("LAS DATA FILTERING TOOL")
print("-" * 50)
selection = input("Should the points INSIDE or OUTSIDE the buffer be deleted? (inside/outside): ").strip().lower()

if selection not in ["inside", "outside", "in", "out"]:
    print("Invalid input. Defaulting to cleaning the INSIDE...")
    selection = "inside"

file_path = r"input_file_path"
print("\nReading shapefile and applying a 5-meter buffer...")
gdf = gpd.read_file(file_path)
merged_buffer = unary_union(gdf.geometry.buffer(5))

las_folder = r"input_folder_path/*.las" 

output_folder = r"output_folder_path"
os.makedirs(output_folder, exist_ok=True)

las_files = glob.glob(las_folder)

if not las_files:
    print("ERROR: No .las files found to process in the specified folder! Check the folder path.")
else:
    for las_path in las_files:
        file_name = os.path.basename(las_path)
        print(f"Processing: {file_name}...")
        
        las = laspy.read(las_path)
        
        points = shapely.points(las.x, las.y)
        is_inside = shapely.contains(merged_buffer, points)
        
        if selection in ["inside", "in"]:
            mask = ~is_inside
        else:
            mask = is_inside
            
        new_las = laspy.create(point_format=las.header.point_format, file_version=las.header.version)
        new_las.points = las.points[mask]
        
        save_path = os.path.join(output_folder, file_name)
        new_las.write(save_path)

    print(f"\nProcess Completed! All cleaned LAS files have been saved to:\n{output_folder}")