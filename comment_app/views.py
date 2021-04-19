from django.shortcuts import render, get_object_or_404
from comment_app.models import Comment
from comment_app.forms import CommentForm
from instaUser_app.models import Profile
from post_app.models import ImageModel
from django.http import HttpResponseForbidden

def EditComment_view(request, comment_id):
    # comment = get_object_or_404(Comment,id=comment_id)
    comment = Comment.objects.all()
    # if request.user.id == comment.user.id:
    if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
            comment.text = data.get(
                'text'
            )
            comment.save()
            return HttpResponseRedirect(f"/postdetail/{comment.image.id}")
    else:
            form = CommentForm()
            return render(request, "edit_comment.html", {'form': form})
    # else:
    #     return HttpResponseForbidden('No Permission To Comment')

# Create your views here.
