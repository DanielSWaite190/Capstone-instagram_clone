from django import forms
# from app_name.models import models


class Profile_eddit(forms.ModelForm):
    class Meta:
        model = user #/Profile
        fields = ['name', 'about'] #anything else we want to change🤷🏾‍♂️


class ImageUplad_form(forms.Form):
    image_file = forms.CharField(max_length=150)
    caption = forms.CharField(max_length=150)
    capture_location = forms.CharField(max_length=150)


class comment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
