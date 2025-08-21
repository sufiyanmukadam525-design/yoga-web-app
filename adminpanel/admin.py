from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from yogaapp.models import Profile
from yogaapp.models import RegisteredUser

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'height', 'weight']
    search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)

=======

# Register your models here.
from yogaapp.models import RegisteredUser

>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "user")
    search_fields = ("username", "email")
<<<<<<< HEAD


=======
    
>>>>>>> 378cfd2d643889c1b7f817a9487d8e62135be505
