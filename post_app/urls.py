from django.urls import path
from django.conf.urls import include, url
from post_app.views import CreatePostView

urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post')
]