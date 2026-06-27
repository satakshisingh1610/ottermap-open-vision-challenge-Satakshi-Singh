import geopandas as gpd

gdf = gpd.read_file("data/annotations/GeoJSON/1.geojson")

print("="*50)
print("Total Bounds")
print("="*50)

print(gdf.total_bounds)

minx, miny, maxx, maxy = gdf.total_bounds

print("\n")

print("Min Longitude :", minx)
print("Max Longitude :", maxx)

print("Min Latitude  :", miny)
print("Max Latitude  :", maxy)

print("\n")

print("Width  :", maxx-minx)
print("Height :", maxy-miny)