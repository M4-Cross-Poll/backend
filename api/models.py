from django.db import models

# Create your models here.
class MuscleGroup(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)


class Activity(models.Model):
    name = models.CharField(max_length=255)
    muscle_groups = models.ManyToManyField(MuscleGroup)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    img_url = models.CharField(max_length=2083)
    muscle_groups = models.ManyToManyField(MuscleGroup)


class User(models.Model):
    username = models.CharField(max_length=255)
    password_digest = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class UserActivity(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    forecast = models.CharField(max_length=255)
    forecast_img = models.CharField(max_length=255)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
