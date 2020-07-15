# Geodistance

Simple program leveraging on Google Maps API to calculate the distance across
multiple locations.

## Setup

### Prerequisites

* `python` >= 3.6
* `pip`
* google account

#### Install pip on Ubuntu

```bash
$ sudo apt install python3-pip
$ pip3 install pip # update pip
```

#### Install virtualenv and other dependencies

```bash
$ pip3 install virtualenv
$ virtualenv --python=$(which python3) .venv
# Activate virtual environment
$ source .venv/bin/activate
# Install new dependecies
(.venv) $ pip install googlemaps
# Dump dependencies
(.venv) $ pip freeze > requirements.txt
# Load dependencies
(.venv) $ pip install -r requirements.txt
```

Please note that if you `which pip`, it should point to `.venv` subfolder.

#### Retrieve google api key and secret

* https://developers.google.com/maps/gmp-get-started
* Create a trial account (300$ free credit)
* copy `.env.example` to `.env` and set the correct value for GOOGLE_API_KEY

## Sample implementation

The purpose of this project is to provide the walking distance between locations.

This can be achieved using the Directions GoogleMapsApi ([see](https://github.com/googlemaps/google-maps-services-python/blob/6682591dda6f987b193bb9b3bdb8e9d50397d651/googlemaps/directions.py#L39-L41)).

### Simplest implementation

The flow could be the following:

1. Provide the target destination lat long
2. Parse/stream a CSV input
3. Foreach lat long, request the walking direction
4. Write the result line by line

### Enhancements

* Store the results into a db (e.g. [SQLite](https://sqlite.org/index.html)): this database is a binary file which can be committed and you may just query origins you haven't calculated yet
* Investigate alternative APIs providing walking distance or alternative approaches (e.g. [Bing API](https://docs.microsoft.com/en-us/bingmaps/rest-services/routes/?toc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fbingmaps%2Frest-services%2Ftoc.json&bc=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2FBingMaps%2Fbreadcrumb%2Ftoc.json), [Pedometer](https://gmap-pedometer.com/))

## References

* https://github.com/googlemaps/google-maps-services-python
* https://virtualenv.pypa.io/en/stable/
* https://pypi.org/project/python-dotenv/
