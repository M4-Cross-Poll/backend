from django.db import models

# Create your models here.
class MuscleGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def primary_exercises(self):
        return Exercise.objects.raw(f"SELECT * FROM api_exercise JOIN api_exercisemusclegroups ON api_exercise.id = api_exercisemusclegroups.exercise_id WHERE api_exercisemusclegroups.muscle_group_id = {self.id} AND api_exercisemusclegroups.type = 'primary' ORDER BY RANDOM() LIMIT 1")

    def secondary_exercises(self):
        return Exercise.objects.raw(f"SELECT * FROM api_exercise JOIN api_exercisemusclegroups ON api_exercise.id = api_exercisemusclegroups.exercise_id WHERE api_exercisemusclegroups.muscle_group_id = {self.id} AND api_exercisemusclegroups.type = 'secondary' ORDER BY RANDOM() LIMIT 1")

class Activity(models.Model):
    name = models.CharField(max_length=255)
    muscle_groups = models.ManyToManyField(MuscleGroup, through='ActivityMuscleGroups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def primary_muscles(self):
        return MuscleGroup.objects.raw(f"SELECT * FROM api_musclegroup JOIN api_activitymusclegroups ON api_activitymusclegroups.muscle_group_id = api_musclegroup.id WHERE api_activitymusclegroups.activity_id = {self.id} AND api_activitymusclegroups.type = 'primary'")

    def secondary_muscles(self):
        return MuscleGroup.objects.raw(f"SELECT * FROM api_musclegroup JOIN api_activitymusclegroups ON api_activitymusclegroups.muscle_group_id = api_musclegroup.id WHERE api_activitymusclegroups.activity_id = {self.id} AND api_activitymusclegroups.type = 'secondary'")


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    img_url = models.CharField(max_length=2083)
    muscle_groups = models.ManyToManyField(MuscleGroup, through='ExerciseMuscleGroups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    equipment = models.CharField(max_length=2000)
    instructions = models.CharField(max_length=2000)


class User(models.Model):
    username = models.CharField(max_length=255)
    password_digest = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def scheduled_activities(self):
        return ScheduledActivity.objects.filter(user=self.id)


class ScheduledActivity(models.Model):
    date = models.CharField(max_length=10, default="yyyy-mm-dd")
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    forecast = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    temp_hi = models.DecimalField(max_digits=5, decimal_places=2)
    temp_low = models.DecimalField(max_digits=5, decimal_places=2)
    precip_probability = models.DecimalField(max_digits=5, decimal_places=2)
    forecast_img = models.CharField(max_length=255)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        bad_weather = ["rain", "snow", "sleet", "wind"]
        if self.forecast_img in bad_weather:
            return "bad"
        return "good"


class ExerciseMuscleGroups(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)


class ActivityMuscleGroups(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
