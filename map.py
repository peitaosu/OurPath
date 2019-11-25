import gmplot 

def get_map_from_coordinate(latitude, longitude, zoom):
    return gmplot.GoogleMapPlotter(latitude, longitude, zoom) 

def get_map_from_geocode(geocode):
    return gmplot.GoogleMapPlotter.from_geocode(geocode)

