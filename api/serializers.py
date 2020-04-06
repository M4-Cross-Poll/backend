from api.models import *
from rest_framework import serializers

class ActivityExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url']


class MuscleGroupSerializer(serializers.ModelSerializer):
    exercise_set = ActivityExerciseSerializer(many=True)

    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'exercise_set']


class ActivitySerializer(serializers.ModelSerializer):
    muscle_groups = MuscleGroupSerializer(many=True)
    class Meta:
        model = Activity
        fields = ['id', 'name', 'muscle_groups']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class UserActivitySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    user = UserSerializer()
    class Meta:
        model = UserActivity
        fields = ['id', 'date', 'location', 'forecast', 'forecast_img', 'activity', 'user', 'created_at', 'updated_at']


class ExerciseSerializer(serializers.ModelSerializer):
    muscle_groups = MuscleGroupSerializer(many=True)
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url', 'muscle_groups']
