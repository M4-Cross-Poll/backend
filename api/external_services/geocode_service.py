import requests
import os
from dotenv import load_dotenv
load_dotenv()

class GeocodeService:

    def get_json(self, uri):
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?{uri}')
        return response.json()

    def get_coordinates(self, location):
        api_key = os.getenv('GEOCODE_API_KEY')
        coordinates_json = self.get_json(f'address={location}&key={api_key}')
        if coordinates_json["status"] == "OK":
            return coordinates_json["results"][0]
        else:
            raise NameError("Invalid Location")
