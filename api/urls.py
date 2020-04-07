from django.urls import path

from . import views

urlpatterns = [
    path('exercises', views.exercise_index, name="exercise_index"),
    path('exercises/<int:exercise_id>', views.exercise_show),
    path('scheduled_activity/<int:scheduled_activity_id>', views.scheduled_activity_show),
]
