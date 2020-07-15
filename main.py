import os
import googlemaps
from dotenv import load_dotenv

from geodistance.models import Coordinate

# Load the content from .env file
load_dotenv()
googleApiKey = os.environ['GOOGLE_API_KEY']
gmaps = googlemaps.Client(key=googleApiKey)

lyon = Coordinate(45.766945, 4.834167)
origin = Coordinate(45.36589813232422, 7.775890827178955)

directions = gmaps.directions(
    origin.toDict(),
    lyon.toDict(),
    mode="walking",
)

if __name__ == "__main__":
    print(lyon)
    print(lyon.latitude)
    print(lyon.longitude)
    print(lyon.toDict())
    print(googlemaps.convert.latlng(origin.toDict()))
    print(directions)
