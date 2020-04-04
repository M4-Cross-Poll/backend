from django.urls import path

from . import views

urlpatterns = [
    path('exercises', views.exercise_index, name="exercise_index")
]
