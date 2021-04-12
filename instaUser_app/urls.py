from django.urls import path
from instaUser_app.views import profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile')
]
