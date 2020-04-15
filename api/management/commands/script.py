from django.core.management.base import BaseCommand
from api.models import ScheduledActivity
from api.external_services.geocode_service import GeocodeService
from api.external_services.darksky_service import DarkskyService
from api.helpers import *
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        current_date = datetime.now().strftime('%Y-%m-%d')
        scheduled_activities = ScheduledActivity.objects.filter(date__gte=current_date)

        for activity in scheduled_activities:
            latitude = f"{activity.latitude}"
            longitude = f"{activity.longitude}"
            date = parse_date(activity.date)
            forecast = DarkskyService().get_forecast(latitude, longitude, date)

            activity.forecast=forecast["daily"]["data"][0]["summary"]
            activity.forecast_img=forecast["daily"]["data"][0]["icon"]
            activity.temperature=forecast["currently"]["temperature"]
            activity.temp_hi=forecast["daily"]["data"][0]["temperatureHigh"]
            activity.temp_low=forecast["daily"]["data"][0]["temperatureLow"]
            activity.precip_probability=forecast["daily"]["data"][0]["precipProbability"]
            activity.save()
