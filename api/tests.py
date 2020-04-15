from django.test import TestCase
from api.external_services.darksky_service import DarkskyService
from api.external_services.geocode_service import GeocodeService
from django.test import Client
from api.models import *
from django.core.management import call_command

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
    def test_it_can_receive_a_request_body_and_create_a_new_activity(self):
        activity = Activity.objects.create(name="Hiking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        c = Client()
        response = c.post(f'/api/v1/users/{user.id}/scheduled_activities/new', {"activity_name": f"{activity.name}", "date": "2020-04-20", "location": "Golden, CO"})

        self.assertEqual(200, response.status_code)

    def test_status_property(self):
        activity = Activity.objects.create(name="Kayaking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        scheduled_activity = ScheduledActivity.objects.create(
            date="2020-04-15",
            location="Denver, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        self.assertEqual("good", scheduled_activity.status)

        scheduled_activity.forecast_img = "rain"
        scheduled_activity.save()

        self.assertEqual("bad", scheduled_activity.status)

        scheduled_activity.forecast_img = "sleet"
        scheduled_activity.save()

        self.assertEqual("bad", scheduled_activity.status)

        scheduled_activity.forecast_img = "cloudy"
        scheduled_activity.save()

        self.assertEqual("good", scheduled_activity.status)

    def test_it_can_be_deleted(self):
        activity = Activity.objects.create(name="Kayaking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        scheduled_activity_1 = ScheduledActivity.objects.create(
            date="2020-04-15",
            location="Denver, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        scheduled_activity_2 = ScheduledActivity.objects.create(
            date="2020-04-19",
            location="Fort Collins, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        c = Client()

        response = c.delete(f'/api/v1/users/{user.id}/scheduled_activities/{scheduled_activity_1.id}')

        self.assertEqual(204, response.status_code)
        self.assertEqual(scheduled_activity_2, ScheduledActivity.objects.all()[0])

    def test_bad_delete_request_returns_404(self):
        activity = Activity.objects.create(name="Kayaking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        scheduled_activity_1 = ScheduledActivity.objects.create(
            date="2020-04-15",
            location="Denver, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        c = Client()

        response = c.delete(f'/api/v1/users/{user.id}/scheduled_activities/5')

        self.assertEqual(404, response.status_code)


class ScheduledActivityManagementCommandTest(TestCase):
    def test_script_commmand(self):
        activity = Activity.objects.create(name="Kayaking")

        user = User.objects.create(username="test_user", first_name="Test", last_name="Name", email="test@example.com")

        scheduled_activity_1 = ScheduledActivity.objects.create(
            date="2020-04-14",
            location="Denver, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        scheduled_activity_2 = ScheduledActivity.objects.create(
            date="2020-04-19",
            location="Fort Collins, CO",
            forecast="Sunny",
            forecast_img="sunny",
            temperature=45.20,
            temp_hi=60.00,
            temp_low=23.00,
            precip_probability=0.07,
            activity=activity,
            user=user
            )

        breakpoint()

        call_command('script')

        breakpoint()
