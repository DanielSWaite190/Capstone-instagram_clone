from django import forms
from phone_field import PhoneField

class Login_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    display_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField(required=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
