from django.contrib import admin
from instaUser_app.models import Profile
from django.contrib.auth.admin import UserAdmin

admin.site.register(Profile, UserAdmin)
