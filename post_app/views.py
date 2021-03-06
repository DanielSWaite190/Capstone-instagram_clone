from django.views.generic import CreateView  # ListView, # new
from django.urls import reverse_lazy  # new
from post_app.models import ImageModel  # new
from post_app.forms import ImageModelForm  # new
from django.contrib.auth.decorators import login_required  # A
from comment_app.models import Comment
from comment_app.forms import CommentForm
# from comment_app.views import EditComment_view not used jk
# from instaUser_app.models import Profile not used jk
from django.shortcuts import render, reverse, HttpResponseRedirect
from comment_app.forms import CommentForm  
from comment_app.views import EditComment_view
from instaUser_app.models import Profile
from django.shortcuts import render, reverse 
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponseForbidden


class CreatePostView(CreateView):  # new
    model = ImageModel
    form_class = ImageModelForm
    template_name = 'post.html'
    success_url = reverse_lazy('home_feed')

    def get_form_kwargs(self):
        kwargs = super(CreatePostView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user.username})
        return kwargs


# A
@login_required
def like_photo_view(request, post_id):
    current_user = request.user
    redirect = request.POST.get('redirect_url', '/')
    post = ImageModel.objects.filter(id=post_id).first()
    post.liked.add(current_user)
    current_user.save()
    return HttpResponseRedirect(redirect)


# A
@login_required
def unlike_photo_view(request, post_id):
    current_user = request.user
    redirect = request.POST.get('redirect_url', '/')
    post = ImageModel.objects.filter(id=post_id).first()
    post.liked.remove(current_user)
    current_user.save()
    return HttpResponseRedirect(redirect)


def PostDetail_View(request, post_id):
    html = 'post_detail.html'
    post = ImageModel.objects.get(id=post_id)
    profileuser = request.user
    comments = Comment.objects.filter(image=post).order_by('-creation_time')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.owner = profileuser
            comment.image = post
            comment.post_id = post_id
            comment.save()

            return HttpResponseRedirect(reverse("post_detail", args=[post_id]))
    else:
        form = CommentForm()
    context = {'owner': post, 'form': form, 'comments': comments}
    return render(request, html, context)



def DeleteComment_view(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if (
        request.user.id == comment.owner.id
    
        or request.user.id == comment.image.author.id):

        comment.delete()
        return HttpResponseRedirect(reverse("post_detail",args = [comment.image.id]))
    else:
        return HttpResponseForbidden('No Permission To Delete Comment')


# A
@login_required
def delete_post_view(request, post_id):
    redirect = request.POST.get('redirect_url', '/')
    post = ImageModel.objects.filter(id=post_id).first()
    post.delete()
    return HttpResponseRedirect(redirect)
    if (
        request.user.id == comment.owner.id
    
        or request.user.id == comment.image.author.id):

        comment.delete()
        return HttpResponseRedirect(reverse("post_detail",args = [comment.image.id]))
    else:
        return HttpResponseForbidden('No Permission To Delete Comment')

    
