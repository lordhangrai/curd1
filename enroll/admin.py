from django.contrib import admin
from .models import User,Resume
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']