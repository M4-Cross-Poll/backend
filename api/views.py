from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from api.models import *
from api.serializers import *
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


def scheduled_activity_show(request, scheduled_activity_id):
    queryset = ScheduledActivity.objects.get(id=scheduled_activity_id)
    serializer = ScheduledActivitySerializer(queryset)
    return JsonResponse(serializer.data)


def user_scheduled_activity_index(request, user_id):
    queryset = User.objects.get(id=user_id)
    # import pdb; pdb.set_trace()
    serializer = UserSerializer(queryset)
    return JsonResponse(serializer.data)
