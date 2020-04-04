from django.shortcuts import render, HttpResponse

# Create your views here.

def exercise_index(request):
    return HttpResponse("You found me")
