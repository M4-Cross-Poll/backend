import requests
import os
from dotenv import load_dotenv
load_dotenv()

class DarkskyService:

    def get_json(self, uri):
        api_key = os.getenv('DARKSKY_API_KEY')
        response = requests.get(f'https://api.darksky.net/forecast/{api_key}/{uri}')
        return response.json()

    def get_forecast(self, lat, lng, time):
        uri = f'{lat},{lng},{time}?exclude=hourly,alerts,flags'
        return self.get_json(uri)
