from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from post_app.models import ImageModel

class HomePageView(ListView):
    model = ImageModel
    template_name = 'home_feed.html'

# class CreatePostView(CreateView): # new
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('home')
