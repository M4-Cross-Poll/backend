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
                                "daily": {
                                    "data": [
                                        {
                                            "time": 255596400,
                                            "summary": "Foggy until morning, starting again in the evening.",
                                            "icon": "cloudy",
                                            "sunriseTime": 255621840,
                                            "sunsetTime": 255659220,
                                            "moonPhase": 0.98,
                                            "precipIntensity": 0,
                                            "precipIntensityMax": 0,
                                            "precipProbability": 0,
                                            "temperatureHigh": 47.44,
                                            "temperatureHighTime": 255650160,
                                            "temperatureLow": 25.41,
                                            "temperatureLowTime": 255682680,
                                            "apparentTemperatureHigh": 43.4,
                                            "apparentTemperatureHighTime": 255650100,
                                            "apparentTemperatureLow": 17.4,
                                            "apparentTemperatureLowTime": 255710940,
                                            "dewPoint": 25.32,
                                            "humidity": 0.8,
                                            "pressure": 1009.5,
                                            "windSpeed": 5.18,
                                            "windBearing": 18,
                                            "cloudCover": 0.9,
                                            "uvIndex": 3,
                                            "uvIndexTime": 255641100,
                                            "visibility": 2.843,
                                            "temperatureMin": 26.13,
                                            "temperatureMinTime": 255679200,
                                            "temperatureMax": 47.44,
                                            "temperatureMaxTime": 255650160,
                                            "apparentTemperatureMin": 19.16,
                                            "apparentTemperatureMinTime": 255671640,
                                            "apparentTemperatureMax": 43.4,
                                            "apparentTemperatureMaxTime": 255650100
                                        }
                                    ]
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
        Activity.objects.create(name="Hiking")
        Activity.objects.create(name="Mountain Biking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        c = Client()
        response = c.post(f'/api/v1/users/{user.id}/scheduled_activities/new', {"activity_name": "Hiking", "date": "2020-04-20", "location": "Golden, CO"})

        self.assertEqual(200, response.status_code)
