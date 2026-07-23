# LAS Buffer Filter

A spatial filtering tool for LiDAR/LAS point cloud data. This script uses a shapefile to create a buffer zone and allows the user to interactively filter out or keep `.las` points that fall inside or outside this buffer. 

It is highly useful for cleaning up point cloud data around specific features (e.g., removing vegetation points near power lines or roads).

## Features
- **Batch Processing:** Automatically finds and processes all `.las` files in a given directory.
- **Interactive Filtering:** Prompts the user to choose whether to delete points *inside* or *outside* the defined buffer.
- **Spatial Precision:** Uses `geopandas` and `shapely` to apply a 5-meter buffer to the input shapefile geometries.
- **Fast Execution:** Handles millions of points efficiently using `laspy` and boolean masking.

## Prerequisites
- Python 3.x
- `geopandas`
- `shapely`
- `laspy`

Install the required dependencies using:
`pip install -r requirements.txt`

## Usage
1. Open the `las_filter.py` script in your editor.
2. Update the hardcoded file paths in the script to match your local directories:
   - `file_path`: Path to your input `.shp` file.
   - `las_folder`: Directory containing your input `.las` files.
   - `output_folder`: Directory where cleaned `.las` files will be saved.
3. Run the script from your terminal:

`python las_filter.py`

4. Follow the on-screen prompt to select your filtering method (`inside` or `outside`).

## Author
**Nil Işıl**
