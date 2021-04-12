from django.urls import path
from instaUser_app import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('profile/<int:profile_id>/', login_required(views.profile_view.as_view()), name='profile'), #DSW
    path('eddit-profile/<int:profile_id>/', views.EdditProfile_view, name='EdditProfile') #DSW
]