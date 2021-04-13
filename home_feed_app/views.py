from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from post_app.models import ImageModel

class HomePageView(ListView):
    model = ImageModel
    template_name = 'home_feed.html'


def PhotoDetailView(request, photo_id):
    post = ImageModel.objects.get(id=photo_id)
    return render(request, "photo_detail.html", {'post':post})
