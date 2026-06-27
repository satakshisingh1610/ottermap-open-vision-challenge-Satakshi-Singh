import cv2
import geopandas as gpd
from shapely.geometry import Polygon
import os

mask = cv2.imread("outputs/prediction.png", cv2.IMREAD_GRAYSCALE)

contours, _ = cv2.findContours(
    mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

polygons = []

for cnt in contours:

    if len(cnt) >= 3:

        pts = [(int(p[0][0]), int(p[0][1])) for p in cnt]

        polygons.append(Polygon(pts))

gdf = gpd.GeoDataFrame(
    {"class": ["Turf"] * len(polygons)},
    geometry=polygons,
    crs="EPSG:4326"
)

os.makedirs("outputs", exist_ok=True)

gdf.to_file(
    "outputs/prediction.geojson",
    driver="GeoJSON"
)

print("GeoJSON Saved!")