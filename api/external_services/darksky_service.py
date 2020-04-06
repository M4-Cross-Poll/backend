import requests
from django.conf import settings

class DarkskyService:

    def get_json(self, uri):
        response = requests.get(f'https://api.darksky.net/forecast/{settings.DARKSKY_API_KEY}/{uri}')
        return response.json()

    def get_forecast(self, lat, lng, time):
        uri = f'{lat},{lng},{time}?exclude=hourly,daily,alerts,flags'
        return self.get_json(uri)
