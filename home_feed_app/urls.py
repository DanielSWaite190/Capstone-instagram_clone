from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from home_feed_app import views

urlpatterns = [
    path('', login_required(views.HomePageView.as_view()), name='home_feed'),
]
