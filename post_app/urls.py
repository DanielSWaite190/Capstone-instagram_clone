from django.urls import path
from post_app.views import CreatePostView
from post_app import views


urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('like/<int:post_id>/', views.like_photo_view, name='like'),  # A
    path('unlike/<int:post_id>/', views.unlike_photo_view, name='unlike'),  # A
]
