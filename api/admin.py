from django.contrib import admin
from .models import Activity, MuscleGroup, Exercise, User, UserActivity
# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'img_url')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password_digest', 'first_name', 'last_name', 'email')


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'location', 'forecast', 'forecast_img', 'activity', 'user')


admin.site.register(Activity, ActivityAdmin)
admin.site.register(MuscleGroup, MuscleGroupAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserActivity, UserActivityAdmin)
