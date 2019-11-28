from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_gps(image_path):
    exif = Image.open(image_path)._getexif()

    if exif:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)
        return exif
    return None

