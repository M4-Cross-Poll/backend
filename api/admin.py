from django.contrib import admin
from .models import *
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img_url', 'equipment', 'instructions', 'created_at', 'updated_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password_digest', 'first_name', 'last_name', 'email', 'created_at', 'updated_at')


class ScheduledActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'location', 'forecast', 'forecast_img', 'activity', 'user', 'created_at', 'updated_at')


class ActivityMuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity_id', 'muscle_group_id')

admin.site.register(Activity, ActivityAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ScheduledActivity, ScheduledActivityAdmin)
admin.site.register(ActivityMuscleGroups, ActivityMuscleGroupAdmin)
