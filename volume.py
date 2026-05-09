import geopandas as gpd
import numpy as np

def compute_volume(water_file):

    water = gpd.read_file(water_file).to_crs(32644)
    contours = gpd.read_file("contours.geojson").to_crs(32644)

    area = water.union_all().area   # m²

    bottom = contours["CONTOUR_ELEVATION"].min()
    top    = contours["CONTOUR_ELEVATION"].max()

    avg_depth = (top - bottom) / 2   # simple approximation

    return float(area * avg_depth)