<<<<<<< HEAD
from django.views.generic import CreateView  # ListView  # new
from django.urls import reverse_lazy  # new
from post_app.models import ImageModel  # new
from post_app.forms import ImageModelForm  # new
from django.shortcuts import HttpResponseRedirect  # A
from django.contrib.auth.decorators import login_required  # A

=======
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from post_app.models import ImageModel # new
from post_app.forms import ImageModelForm # new
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92

class CreatePostView(CreateView):  # new
    model = ImageModel
    form_class = ImageModelForm
    template_name = 'post.html'
    success_url = reverse_lazy('home_feed')
<<<<<<< HEAD


# A
@login_required
def like_photo_view(request, post_id):
    current_user = request.user
    redirect = request.POST.get('redirect_url', '/')
    post = ImageModel.objects.filter(id=post_id).first()
    current_user.likes.add(post)
    current_user.save()
    return HttpResponseRedirect(redirect)


# A
@login_required
def unlike_photo_view(request, post_id):
    current_user = request.user
    redirect = request.POST.get('redirect_url', '/')
    post = ImageModel.objects.filter(id=post_id).first()
    current_user.likes.remove(post)
    current_user.save()
    return HttpResponseRedirect(redirect)
=======
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92
