from django.contrib import admin
from instaUser_app.models import Profile
from django.contrib.auth.admin import UserAdmin

class Profile_Admin(UserAdmin):
    model = Profile
    fieldsets = UserAdmin.fieldsets + (
    (None, {'fields': ('display_name', 'profile_pic',
        'dob', 'phone','bio', 'following')}),
    )

admin.site.register(Profile, Profile_Admin)
