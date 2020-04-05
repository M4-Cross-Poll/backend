from django.contrib import admin
from .models import Activity, MuscleGroup, Exercise, User, UserActivity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img_url', 'created_at', 'updated_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password_digest', 'first_name', 'last_name', 'email', 'created_at', 'updated_at')


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'location', 'forecast', 'forecast_img', 'activity', 'user', 'created_at', 'updated_at')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
