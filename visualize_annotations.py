import cv2
import geopandas as gpd
import matplotlib.pyplot as plt

# Load image
image = cv2.imread("data/images/1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load GeoJSON
gdf = gpd.read_file("data/annotations/GeoJSON/1.geojson")

fig, ax = plt.subplots(figsize=(10,10))

# Show only the polygons first
gdf.boundary.plot(ax=ax, color="red", linewidth=1)

plt.title("GeoJSON Only")
plt.show()