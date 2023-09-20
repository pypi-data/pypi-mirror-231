import requests
import os
# import pprint
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')

# url = f"https://api.openweathermap.org/data/2.5/forecast?q=madrid&APPID={api_key}&units=imperial"
url = f"https://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.4&APPID={api_key}&units=imperial"


class Weather:
    """
    Creates a Weather object getting an apikey as input 
    and either a city name or latitude and longitute coordinates.

    How to use the package?
    # Create a weather object using a city name.
    # Use your own api key from https://openweathermap.org
    # Wait for couple of hours for the apikey to be activated

    >>> weather1 = Weather(apikey=api_key, city="Pleasanton")

    # Using latitude and longitude coordinates
    >>> weather2 = Weather(apikey=api_key, lat = 4.1, lon = 4.5)

    # Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    # Simplified data for the next 12 hours:
    >>> weather1.next_12h_simplified()

    """

    def __init__(self, apikey=api_key, city=None, lat=None, lon=None):
        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")
        # if city is not found
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"])

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for dicty in self.data['list'][:4]:            
            simple_data.append((dicty['dt_txt'],dicty['main']['temp'], dicty['weather'][0]['description'] )) 
        return simple_data

# weather = Weather(city="Pleasanton", lat = 4.1, lon = 4.5)
# print(weather.data)
# pprint.pprint(weather.next_12h_simplified())