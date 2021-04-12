from django.urls import path
<<<<<<< HEAD
from instaUser_app.views import profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile')
=======
from instaUser_app import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('profile/<int:profile_id>/', login_required(views.profile_view.as_view()), name='profile'), #DSW
    path('eddit-profile/<int:profile_id>/', views.EdditProfile_view, name='EdditProfile') #DSW
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92
]
