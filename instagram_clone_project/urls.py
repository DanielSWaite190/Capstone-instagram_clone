from django.contrib import admin
from django.urls import path, include
from auth_app import views
from home_feed_app import views
from django.conf import settings
from django.conf.urls.static import static
from post_app import views
from home_feed_app.urls import urlpatterns as home_url
from auth_app.urls import urlpatterns as auth_url
from post_app.urls import urlpatterns as post_url


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += home_url
urlpatterns += auth_url
urlpatterns += post_url

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
