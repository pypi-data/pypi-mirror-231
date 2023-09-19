import requests


class Weather:
    """Creates a Weather object getting an apikey as input and
    either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # The api key below is not guaranteed to work.
    # Get your own apikey from https://openweathermap.org
    # And wait a couple of hours for the apikey to be activated

    # >>> weather1 = Weather(apikey = 'b12412447526be89f5c1dfe4943723d7', city = "Madrid")

    # Using latitude and longitude coordinates
    # >>> weather2 = Weather(apikey = 'b12412447526be89f5c1dfe4943723d7', lat=31.2,  lon=2.1)

    # Get complete weather data for the next 12 hours:
    # >>> weather1.next_12h()

    # Simplified data for the next 12hours:
    # >>> weather1.next12h_simplified()

    """
    def __init__(self, api_key, city=None, lat=None, lon=None):
        self.city = city.replace(" ", "-")
        self.lat = lat
        self.lon = lon
        if city:
            r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?"
                             f"q={city}"
                             f"&appid={api_key}&"
                             f"units=metric")
            self.data = r.json()
        elif lat and lon:
            r = requests.get(f"https://pro.openweathermap.org/data/2.5/forecast/hourly?"
                             f"lat={lat}&"
                             f"lon={lon}&"
                             f"appid={api_key}&"
                             f"units=metric")
            self.data = r.json()
        else:
            raise TypeError("Please provide either a city name or a lat/lon argument")

        if self.data['cod'] != "200":
            raise ValueError(self.data['message'])

    def next_12h(self):
        try:
            return self.data['list'][:4]
        except TypeError:
            print("Please provide either a city name or a lat/lon argument")

    def next12h_simplified(self):
        dic = {}
        for forecast in self.data['list'][:4]:
            dic[forecast['dt_txt']] = (forecast['main']['temp'], forecast['weather'][0]['description'])
        return dic
