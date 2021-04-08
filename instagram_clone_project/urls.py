from django.contrib import admin
from django.urls import path, include
from auth_app import views
from home_feed_app import views

urlpatterns = [
    path('', include('auth_app.urls')),
    path('home/', include('home_feed_app.urls')),
    path('admin/', admin.site.urls)
]
