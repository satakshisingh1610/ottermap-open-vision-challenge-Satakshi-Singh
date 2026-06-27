import os
import cv2
import numpy as np
import geopandas as gpd

IMAGE_FOLDER = "data/images"
GEOJSON_FOLDER = "data/annotations/GeoJSON"
MASK_FOLDER = "data/masks"

os.makedirs(MASK_FOLDER, exist_ok=True)

for image_file in os.listdir(IMAGE_FOLDER):

    base = os.path.splitext(image_file)[0]

    geojson_path = os.path.join(GEOJSON_FOLDER, base + ".geojson")
    image_path = os.path.join(IMAGE_FOLDER, image_file)

    print(f"\nProcessing {base}")

    image = cv2.imread(image_path)

    if image is None:
        print("Cannot read image.")
        continue

    h, w = image.shape[:2]

    gdf = gpd.read_file(geojson_path)

    minx, miny, maxx, maxy = gdf.total_bounds

    mask = np.zeros((h, w), dtype=np.uint8)

    for geom in gdf.geometry:

        if geom.geom_type == "Polygon":
            polys = [geom]

        elif geom.geom_type == "MultiPolygon":
            polys = list(geom.geoms)

        else:
            continue

        for poly in polys:

            coords = np.array(poly.exterior.coords)

            pixel_points = []

            for lon, lat in coords:

                x = int((lon - minx) / (maxx - minx) * (w - 1))

                y = int((maxy - lat) / (maxy - miny) * (h - 1))

                pixel_points.append([x, y])

            pixel_points = np.array(pixel_points, dtype=np.int32)

            cv2.fillPoly(mask, [pixel_points], 255)

    save_path = os.path.join(MASK_FOLDER, base + "_mask.png")

    cv2.imwrite(save_path, mask)

    print("Saved:", save_path)

print("\nDone!")