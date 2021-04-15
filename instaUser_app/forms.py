from django import forms
from instaUser_app.models import Profile

#DSW
class ProfileEdditForm(forms.Form):
    profile_pic = forms.ImageField()
    display_name = forms.CharField(max_length=75)
    bio = forms.CharField(max_length=40)
    dob = forms.DateField()
