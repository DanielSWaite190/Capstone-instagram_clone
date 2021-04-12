from django.urls import path
from post_app.views import CreatePostView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('post/', login_required(CreatePostView.as_view()), name='add_post')
]