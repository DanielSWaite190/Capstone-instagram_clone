from django import forms
from phone_field import PhoneField


class Login_form(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.Form):
    display_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Displayname'}))
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Example@gmail.com'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    dob = forms.DateField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    phone = PhoneField(blank=True, help_text='Contact phone number')
