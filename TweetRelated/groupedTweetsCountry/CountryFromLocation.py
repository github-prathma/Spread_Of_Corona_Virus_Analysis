# This file is gives the countries for every user location.
# The output is stored in groupedTweetsCountry/tweetsCountry.csv

import time

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import pandas as pd
from geopy.extra.rate_limiter import RateLimiter
from requests import HTTPError

geolocator = Nominatim(user_agent="geoCode", timeout=10)

df = pd.read_csv("../CleanedTweetsInfo.csv", usecols=["Tweet_id", "UserLocation", "Tweet_content"],
                 dtype={"Tweet_id": "object", "UserLocation": "object"})

fp = open("tweetsCountry.csv", "w+")


def do_geocode(address):
    try:
        location = geolocator.geocode(address, featuretype="Country")
        fp.write(str(location))
        fp.write("\n")
        if location is not None:
            return location.address.rpartition(',')[2]
        else:
            return None
    except HTTPError as e:
        print(e)
        print("Sleeping for 15 minutes....")
        time.sleep(60 * 15 + 5)
        print("After 15 minutes....")
        return do_geocode(address)

    except GeocoderTimedOut:
        print("Sleeping for 15 minutes....")
        time.sleep(60 * 15 + 5)
        print("After 15 minutes....")
        return do_geocode(address)


def get_Country_from_location(df):
    geocodeLimiter = RateLimiter(do_geocode, min_delay_seconds=1)
    locationCountryDictionary = {}
    unique_loc = df['UserLocation']
    for loc in unique_loc:
        if loc not in locationCountryDictionary.keys():
            locationCountryDictionary[loc] = geocodeLimiter(loc)
        else:
            locationCountryDictionary[loc] = locationCountryDictionary.get(loc)


# Comment this once run to avoid overwriting file
# get_Country_from_location(df)
fp.close()
