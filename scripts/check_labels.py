import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file("data/annotations/GeoJSON/1.geojson")

print(gdf)

fig, ax = plt.subplots(figsize=(8,8))

gdf.plot(ax=ax,color="green",alpha=0.5)

plt.title("Turf Polygons")

plt.show()