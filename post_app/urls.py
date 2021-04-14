from django.urls import path
from django.contrib.auth.decorators import login_required
from post_app import views

urlpatterns = [
    path('post/', login_required(views.CreatePostView.as_view()), name='add_post'),
    path('like/<int:post_id>/', views.like_photo_view, name='like'),  # A
    path('unlike/<int:post_id>/', views.unlike_photo_view, name='unlike'),  # A
]
