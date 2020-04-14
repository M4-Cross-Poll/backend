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


class PrimaryMuscleGroupSerializer(serializers.ModelSerializer):
    primary_exercises = ActivityExerciseSerializer(many=True)
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'primary_exercises']


class SecondaryMuscleGroupSerializer(serializers.ModelSerializer):
    secondary_exercises = ActivityExerciseSerializer(many=True)
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name', 'secondary_exercises']


class ActivitySerializer(serializers.ModelSerializer):
    # muscle_groups = MuscleGroupSerializer(many=True)
    primary_muscles = PrimaryMuscleGroupSerializer(many=True)
    secondary_muscles = SecondaryMuscleGroupSerializer(many=True)
    class Meta:
        model = Activity
        fields = ['id', 'name', 'primary_muscles', 'secondary_muscles']


class ScheduledActivityIndexSerializer(serializers.ModelSerializer):
    activity = serializers.StringRelatedField()
    class Meta:
        model = ScheduledActivity
        fields = ['id', 'activity', 'date', 'location', 'forecast', 'forecast_img']


class UserSerializer(serializers.ModelSerializer):
    scheduled_activities = ScheduledActivityIndexSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'scheduled_activities']


class ScheduledActivitySerializer(serializers.ModelSerializer):
    activity = ActivitySerializer()
    user = UserSerializer()
    class Meta:
        model = ScheduledActivity
        fields = ['id', 'date', 'location', 'forecast', 'forecast_img', 'temperature', 'temp_hi', 'temp_low', 'precip_probability', 'activity', 'user', 'created_at', 'updated_at']


class ExerciseMuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = ['id', 'name']


class ExerciseSerializer(serializers.ModelSerializer):
    muscle_groups = ExerciseMuscleGroupSerializer(many=True)
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url', 'equipment', 'instructions', 'muscle_groups', 'primary_muscles', 'secondary_muscles']


class ExerciseIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'img_url', 'equipment', 'instructions']


class ActivityIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name']
