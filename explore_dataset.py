import os
import cv2
import rasterio
import geopandas as gpd

# -------------------------------
# IMAGE INFORMATION
# -------------------------------

print("=" * 60)
print("IMAGE INFORMATION")
print("=" * 60)

image_folder = "data/images"

for file in os.listdir(image_folder):

    path = os.path.join(image_folder, file)

    if file.endswith(".jpg") or file.endswith(".png"):

        img = cv2.imread(path)

        h, w, c = img.shape

        print(f"\nImage : {file}")
        print(f"Width : {w}")
        print(f"Height: {h}")
        print(f"Channels: {c}")

    elif file.endswith(".tif") or file.endswith(".tiff"):

        with rasterio.open(path) as src:

            print(f"\nImage : {file}")
            print(f"Width : {src.width}")
            print(f"Height: {src.height}")
            print(f"Bands : {src.count}")
            print(f"CRS   : {src.crs}")

# -------------------------------
# GEOJSON INFORMATION
# -------------------------------

print("\n")
print("=" * 60)
print("GEOJSON INFORMATION")
print("=" * 60)

annotation_folder = "data/annotations/GeoJSON"

print("Folder Exists :", os.path.exists(annotation_folder))
print("Files Found :", os.listdir(annotation_folder))

for file in os.listdir(annotation_folder):

    if file.endswith(".geojson"):

        path = os.path.join(annotation_folder, file)

        gdf = gpd.read_file(path)

        print("\n" + "=" * 60)
        print(f"File : {file}")
        print("=" * 60)

        print(f"Total Features : {len(gdf)}")
        print("Columns :", list(gdf.columns))

        print("\nFirst 5 Rows:")
        print(gdf.head())

        print("\nGeometry Type:")
        print(gdf.geometry.geom_type.unique())

        print("\nCRS:")
        print(gdf.crs)

        print("\nFirst Geometry:")
        print(gdf.geometry.iloc[0])