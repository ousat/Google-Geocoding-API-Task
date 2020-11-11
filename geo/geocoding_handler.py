import googlemaps
import time
import random
from geoUpdater.google_api_config import GOOGLE_API_KEY

def get_client():
    '''
    returns google maps client authorized by the API KEY set in google_api_config file
    '''
    return googlemaps.Client(key=GOOGLE_API_KEY)

def get_lat_long_from_address(address_string, gmaps_client):
    '''
    returns latitude and longitude values for the input address
    '''
    try:
        geomaps_data = gmaps_client.geocode(address_string)

        try:
            lat = geomaps_data[0]['geometry']['location']['lat']
        except (KeyError, IndexError):
            lat = None

        try:
            lng = geomaps_data[0]['geometry']['location']['lng']
        except (KeyError, IndexError):
            lng = None
        # print(lat)
        # print(lng)
        return lat, lng
    except Exception as e:
        # print(e)
        
        # in case of API/ internet errors waiting for random seconds and retrying
        try:
            time.sleep(5*int(random.random()*10))
            lat, lng = get_lat_long_from_address(address_string, gmaps_client)
        except RecursionError:
            # on too many retries and failures returning None values for latitude and longitude
            return None, None



