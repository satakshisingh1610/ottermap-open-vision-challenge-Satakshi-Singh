import os
import rasterio

image_folder = "data/images"

for file in os.listdir(image_folder):

    if file.endswith(".tif") or file.endswith(".tiff"):

        path = os.path.join(image_folder, file)

        with rasterio.open(path) as src:

            print("="*60)
            print(file)
            print("="*60)

            print("CRS:", src.crs)
            print("Bounds:", src.bounds)
            print("Transform:\n", src.transform)