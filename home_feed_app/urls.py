from django.contrib import admin
from django.urls import path
from home_feed_app import views

urlpatterns = [
    path('', views.home, name='home_feed')
]
