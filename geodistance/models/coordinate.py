class Coordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # Format as accepted origin/destination input
    # for googlemaps.convert
    # https://github.com/googlemaps/google-maps-services-python/blob/d39ff32820a8e77e2f789af81590fcc3a3770797/googlemaps/convert.py#L84-L108
    def toDict(self) -> dict:
        return {'lat': self.latitude, 'lng': self.longitude}
