from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_gps(image_path):
    exif = Image.open(image_path)._getexif()

    if exif:
        for key, value in exif.items():
            name = TAGS.get(key, key)
            exif[name] = exif.pop(key)

        if 'GPSInfo' in exif:
            for key in exif['GPSInfo'].keys():
                name = GPSTAGS.get(key,key)
                exif['GPSInfo'][name] = exif['GPSInfo'].pop(key)
            return exif['GPSInfo']
    return None

def get_formatted_gps_info(gps_info):
    latitude = gps_info['GPSLatitude']
    latitude_ref = gps_info['GPSLatitudeRef']
    latitude_str = (str(latitude[0][0]/latitude[0][1]) + '°' + str(latitude[1][0]/latitude[1][1]) + '′' + str(latitude[2][0]/latitude[2][1]) + '″ ' + latitude_ref )
    longitude = gps_info['GPSLongitude']
    longitude_ref = gps_info['GPSLongitudeRef']
    longitude_str = (str(longitude[0][0]/longitude[0][1]) + '°' + str(longitude[1][0]/longitude[1][1]) + '′' + str(longitude[2][0]/longitude[2][1]) + '″ ' + longitude_ref )
    return (latitude_str, longitude_str)
