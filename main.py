import csv
import json
import os
from pathlib import Path
# import pdb # debugger
import time

from dotenv import load_dotenv # .env file parser
import googlemaps # google API client

from geodistance.models import Coordinate

# Load the content from .env file
load_dotenv()
googleApiKey = os.environ['GOOGLE_API_KEY']
gmaps = googlemaps.Client(key=googleApiKey)

# CSV input file
currentTimestamp = int(time.time())

originsFile = Path("data/distance_origin_destination.csv")
outputFile = Path("data/output-{}.csv".format(currentTimestamp))
outputFolder = Path("data/raw_directions/")

# For this project is enough to provide always LYON as destination
LYON = Coordinate(45.766945, 4.834167)

def getDirections(client, origin, destination=LYON):
    return client.directions(
        origin.toDict(),
        destination.toDict(),
        mode="walking",
    )

fieldNames = ['idcom', 'latitude', 'longitude', 'distance_m', 'duration_sec']

def processRow(client, row):
    rawRowFile = os.path.join(outputFolder, "{}.json".format(row['idcom']))

    print("Processing {}".format(rawRowFile))
    # check if the raw response has already been saved on file system
    if os.path.isfile(rawRowFile):
        print("Reading from cache")
        with open(rawRowFile) as cachedResponse:
            response = json.load(cachedResponse)
    else:
        print("Calling Google API")
        response = getDirections(client, Coordinate(row['latitude'], row['longitude']))
        with open(rawRowFile, 'w') as f:
            json.dump(response, f)

    return {
        'idcom': row['idcom'],
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'distance_m': response[0]['legs'][0]['distance']['value'],
        'duration_sec': response[0]['legs'][0]['duration']['value']
    }

def main(originsFile, outputFile, gmapsClient=gmaps, output=[], fieldNames=fieldNames):
    with open(originsFile, mode = 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            try:
                output.append(processRow(gmapsClient, row))
            except IndexError:
                with open("errors.txt", 'a') as err:
                    err.write("{}\n".format(row['idcom']))

    with open(outputFile, mode = 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

        writer.writeheader()
        while output:
            writer.writerow(output.pop(0))

if __name__ == "__main__":
    main(originsFile, outputFile)
