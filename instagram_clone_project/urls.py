from django.contrib import admin
from django.urls import path, include
from auth_app import views
from home_feed_app import views
from django.conf import settings
from django.conf.urls.static import static
from home_feed_app.urls import urlpatterns as home_url

urlpatterns = [
    # path('', include('auth_app.urls')),
    # path('', include('home_feed_app.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += home_url

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
