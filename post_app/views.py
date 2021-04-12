from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy # new
from post_app.models import ImageModel # new
from post_app.forms import ImageModelForm # new
<<<<<<< HEAD
# Create your views here.

=======
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92

class CreatePostView(CreateView): # new
    model = ImageModel
    form_class = ImageModelForm
    template_name = 'post.html'
<<<<<<< HEAD
    success_url = reverse_lazy('home_feed')
=======
    success_url = reverse_lazy('home_feed')
>>>>>>> 479dc0d1196ad9795d45af1bf9c03096690bea92
