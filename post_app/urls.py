from django.urls import path
from post_app.views import CreatePostView

urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post')
]
