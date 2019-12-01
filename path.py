from gps import *
from map import *
from exif import *
import os, sys

image_path = sys.argv[1]
exif = get_exif(image_path)
gps = get_gps(exif)
map = get_map_gps_info(gps)
map.draw()
