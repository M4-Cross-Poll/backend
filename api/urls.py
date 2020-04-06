from django.urls import path

from . import views

urlpatterns = [
    path('exercises', views.exercise_index, name="exercise_index"),
    path('exercises/<int:exercise_id>', views.exercise_show),
    path('user_activities/<int:user_activity_id>', views.user_activity),
]
