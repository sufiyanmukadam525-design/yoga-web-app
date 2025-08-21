from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from yogaapp.models import Profile, RegisteredUser


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'height', 'weight']
    search_fields = ['user__username']


admin.site.register(Profile, ProfileAdmin)


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "user")
    search_fields = ("username", "email")
