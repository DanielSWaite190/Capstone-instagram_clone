from django import forms
# from instaUser_app.models import Profile jk not used


# DSW
class ProfileEdditForm(forms.Form):
    profile_pic = forms.ImageField()
    display_name = forms.CharField(
        max_length=75,
        widget=forms.TextInput(attrs={'placeholder': 'Displayname'}))
    bio = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder': 'Bio'}))
    dob = forms.DateField(
        widget=forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}))
