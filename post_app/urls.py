from django.urls import path
from post_app.views import CreatePostView
<<<<<<< HEAD

urlpatterns = [
    path('post/', CreatePostView.as_view(), name='add_post')
=======
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('post/', login_required(CreatePostView.as_view()), name='add_post')
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92
]
