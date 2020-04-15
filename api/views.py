from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api.models import *
from api.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.external_services.geocode_service import GeocodeService
from api.external_services.darksky_service import DarkskyService
from api.helpers import *

# Create your views here.

def exercise_index(request):
    queryset = Exercise.objects.all()
    serializer = ExerciseIndexSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)


def exercise_show(request, exercise_id):
    queryset = Exercise.objects.get(id=exercise_id)
    primary_muscles = queryset.primary_muscles
    serializer = ExerciseSerializer(queryset)
    return JsonResponse(serializer.data)


def activity_index(request):
    queryset = Activity.objects.all()
    serializer = ActivityIndexSerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'DELETE'])
def scheduled_activity(request, user_id, scheduled_activity_id):
    if request.method == 'GET':
        try:
            queryset = ScheduledActivity.objects.get(id=scheduled_activity_id)
        except:
            return JsonResponse('Record not found', status=404, safe=False)

        serializer = ScheduledActivitySerializer(queryset)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        try:
            scheduled_activity = ScheduledActivity.objects.get(id=scheduled_activity_id)
        except:
            return JsonResponse('Record not found', status=404, safe=False)

        try:
            scheduled_activity.delete()
            return JsonResponse('Deleted successfully', status=204, safe=False)
        except:
            return JsonResponse('Unable to delete record', status=500, safe=False)

def user_scheduled_activity_index(request, user_id):
    queryset = User.objects.get(id=user_id)
    serializer = UserSerializer(queryset)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def create_scheduled_activity(request, user_id):
    activity = Activity.objects.get(name=request.data["activity_name"])
    date = parse_date(request.data["date"])
    location = request.data["location"]
    user = User.objects.get(id=user_id)

    coordinates = GeocodeService().get_coordinates(location)

    forecast = DarkskyService().get_forecast(coordinates["lat"], coordinates["lng"], date)

    new_scheduled_activity = ScheduledActivity.objects.create(
        date=request.data["date"],
        location=location,
        latitude = coordinates["lat"],
        longitude = coordinates["lng"],
        forecast=forecast["daily"]["data"][0]["summary"],
        forecast_img=forecast["daily"]["data"][0]["icon"],
        temperature=forecast["currently"]["temperature"],
        temp_hi=forecast["daily"]["data"][0]["temperatureHigh"],
        temp_low=forecast["daily"]["data"][0]["temperatureLow"],
        precip_probability=forecast["daily"]["data"][0]["precipProbability"],
        activity=activity,
        user=user
        )

    serializer = ScheduledActivitySerializer(new_scheduled_activity)
    return JsonResponse(serializer.data, safe=False)
