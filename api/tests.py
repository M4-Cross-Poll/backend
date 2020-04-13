from django.test import TestCase
from api.external_services.darksky_service import DarkskyService
from api.external_services.geocode_service import GeocodeService
from django.test import Client
from api.models import *
# Create your tests here.

class DarkskyServiceTestCase(TestCase):
    def test_service_returns_json_of_forecast(self):
        expected_response = {
                                "latitude": 39.742043,
                                "longitude": -104.991531,
                                "timezone": "America/Denver",
                                "currently": {
                                    "time": 255657600,
                                    "summary": "Overcast",
                                    "icon": "cloudy",
                                    "precipIntensity": 0,
                                    "precipProbability": 0,
                                    "temperature": 36.84,
                                    "apparentTemperature": 28.68,
                                    "dewPoint": 26.83,
                                    "humidity": 0.67,
                                    "pressure": 1005.5,
                                    "windSpeed": 12.47,
                                    "windBearing": 8,
                                    "cloudCover": 1,
                                    "uvIndex": 0,
                                    "visibility": 9.997
                                },
                                "offset": -7
                            }


        service = DarkskyService()
        response = service.get_forecast('39.742043','-104.991531','255657600')
        self.assertEqual(response, expected_response)


class GeocodeServiceTestCase(TestCase):
    def test_service_returns_hash_of_latitude_and_longitude_for_location(self):
        expected_response = {
                            "lat": 39.7392358,
                            "lng": -104.990251
                            }

        service = GeocodeService()
        response = service.get_coordinates('denver,co')
        self.assertEqual(response, expected_response)


class NewScheduledActivity(TestCase):
    def test_it_can_receive_a_request_body(self):
        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        c = Client()
        response = c.post(f'/api/v1/users/{user.id}/scheduled_activities/new', {"activity_name": "Hiking", "date": "2020-04-20", "location": "Golden, CO"})

        self.assertEqual("this should be good", response)
