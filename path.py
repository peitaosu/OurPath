from gps import *
from map import *
from exif import *
import os, sys

image_path = sys.argv[1]
exif = get_exif(image_path)
if exif:
    gps = get_gps(exif)
    get_map_gps_info(gps).draw()
else:
    print("No exif found")
