from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from post_app.models import ImageModel

class HomePageView(ListView):
    model = ImageModel
    template_name = 'home_feed.html'
    
    # def get_queryset(self):
    #     comments = Comment.objects.filter(image=self.kwargs['image_id'])
    #     all_comments = get_children_recursive(category)
    #     return Product.objects.filter(categories=all_children)