from django.urls import path

from . import views

urlpatterns = [
    path('exercises', views.exercise_index, name="exercise_index"),
    path('exercises/<int:exercise_id>', views.exercise_show),
    path('scheduled_activities/<int:scheduled_activity_id>', views.scheduled_activity_show),
    path('activities', views.activity_index),
    path('<int:user_id>/scheduled_activities', views.user_scheduled_activity_index),
    path('users/<int:user_id>/scheduled_activities/new', views.create_scheduled_activity),
]
