from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from post_app.models import ImageModel

# @login_required
# def home(request):
#     return render(request, "home_feed_app/home_feed.html")






class HomePageView(ListView):
    model = ImageModel
    template_name = 'home_feed.html'
    

# class CreatePostView(CreateView): # new
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('home')
