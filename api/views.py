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
    try:
        activity = Activity.objects.get(name=request.data["activity_name"])
        user = User.objects.get(id=user_id)
    except Activity.DoesNotExist:
        return JsonResponse(f"Activity with that name could not be found.", status=404, safe=False)
    except User.DoesNotExist:
        return JsonResponse(f"User with ID {user_id} could not be found.", status=404, safe=False)

    location_input = request.data["location"]

    try:
        location_data = GeocodeService().get_coordinates(location_input)
    except NameError:
        return JsonResponse(f"The location provided could not be geocoded. Please be more specific (include state or country).", status=500, safe=False)

    try:
        date = parse_date(request.data["date"])
        forecast = DarkskyService().get_forecast(location_data["geometry"]["location"]["lat"], location_data["geometry"]["location"]["lng"], date)
    except:
        return JsonResponse("The date provided could not be parsed correctly. Please ensure it is in the format of 'YYYY-MM-DD'", status=400, safe=False)

    try:
        new_scheduled_activity = ScheduledActivity.objects.create(
            date=request.data["date"],
            location=parse_location(location_data["formatted_address"]),
            latitude = location_data["geometry"]["location"]["lat"],
            longitude = location_data["geometry"]["location"]["lng"],
            forecast=forecast["daily"]["data"][0]["summary"],
            forecast_img=forecast["daily"]["data"][0]["icon"],
            temperature=forecast["currently"]["temperature"],
            temp_hi=forecast["daily"]["data"][0]["temperatureHigh"],
            temp_low=forecast["daily"]["data"][0]["temperatureLow"],
            precip_probability=forecast["daily"]["data"][0]["precipProbability"],
            activity=activity,
            user=user
            )
    except:
        return JsonResponse("An error occurred while trying to create the scheduled_activity", status=500, safe=False)

    serializer = ScheduledActivitySerializer(new_scheduled_activity)
    return JsonResponse(serializer.data, safe=False)
