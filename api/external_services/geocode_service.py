import requests
# from django.conf import settings


class GeocodeService:


    def get_json(self, uri):
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?{uri}')
        return response.json()

    def get_coordinates(self, location):
        coordinates_json = self.get_json(f'address={location}&key=AIzaSyD4277ZEyw5R_B-Gk2ZfS3BfMemEFK-Is8')
        

# service = GeocodeService()
# service.get_coordinates('denver,co')
#
# import pdb; pdb.set_trace()
