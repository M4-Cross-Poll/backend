from api.models import *
from rest_framework import serializers

class ActivityExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url', 'equipment', 'instructions']


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


class ScheduledActivitySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    user = UserSerializer()
    class Meta:
        model = ScheduledActivity
        fields = ['id', 'date', 'location', 'forecast', 'forecast_img', 'activity', 'user', 'created_at', 'updated_at']


class ExerciseMuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name']

class ExerciseSerializer(serializers.ModelSerializer):
    muscle_groups = ExerciseMuscleGroupSerializer(many=True)
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url', 'equipment', 'instructions', 'muscle_groups']
