from django import forms
from instaUser_app.models import Profile

#DSW
class ProfileEdditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'display_name',
            'profile_pic',
            'dob',
            'phone',
            'bio',
            'following'
            ]
