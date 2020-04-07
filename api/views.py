from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api.models import *
from api.serializers import *
# Create your views here.

def exercise_index(request):
    return HttpResponse("You found me")

def exercise_show(request, exercise_id):
    queryset = Exercise.objects.get(id=exercise_id)
    serializer = ExerciseSerializer(queryset)
    return JsonResponse(serializer.data)

def scheduled_activity_show(request, scheduled_activity_id):
    queryset = ScheduledActivity.objects.get(id=scheduled_activity_id)
    serializer = ScheduledActivitySerializer(queryset)
    return JsonResponse(serializer.data)
