from django.urls import path
from django.contrib.auth.decorators import login_required
from post_app import views
from post_app.views import CreatePostView, PostDetail_View, DeleteComment_view
from comment_app.views import EditComment_view
    
urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('editcomment/<int:comment_id>/', EditComment_view, name='edit_comment'),
    path('postdetail/<int:post_id>/', PostDetail_View, name='post_detail'),
    path('deletecomment/<int:comment_id>/', DeleteComment_view, name='delete_comment'),
    path('like/<int:post_id>/', views.like_photo_view, name='like'),  # A
    path('unlike/<int:post_id>/', views.unlike_photo_view, name='unlike')  # A
]
