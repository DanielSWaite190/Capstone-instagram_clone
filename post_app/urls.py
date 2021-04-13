from django.urls import path
from post_app.views import CreatePostView
<<<<<<< HEAD
from post_app import views


urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('like/<int:post_id>/', views.like_photo_view, name='like'),  # A
    path('unlike/<int:post_id>/', views.unlike_photo_view, name='unlike'),  # A
=======
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('post/', login_required(CreatePostView.as_view()), name='add_post')
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92
]
