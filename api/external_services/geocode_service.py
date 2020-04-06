import requests
# from django.conf import settings


class GeocodeService:


    def get_json(self, uri):
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?{uri}')
        return response.json()

    # returns a hash of lat: and long:
    def get_coordinates(self, location):
        coordinates_json = self.get_json(f'address={location}&key=AIzaSyD4277ZEyw5R_B-Gk2ZfS3BfMemEFK-Is8')
        return coordinates_json["results"][0]["geometry"]["location"]
