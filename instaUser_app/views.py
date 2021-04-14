from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from instaUser_app.forms import ProfileEdditForm
from instaUser_app.models import Profile
from post_app.models import ImageModel  # Ana
from django.views import View


# DSW Update
class profile_view(View):
    template_name = "profile.html"

    def get(self, request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        return render(request, self.template_name, {'profile': profile})


# DSW
@login_required
def EdditProfile_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {}  # I might not need this
    initial = {
        'display_name': profile.display_name,
        'profile_pic': profile.profile_pic,
        'dob': profile.dob,
        'phone': profile.phone,
        'bio': profile.bio
    }

    if request.method == "POST":
        form = ProfileEdditForm(request.POST, instance=profile)
        if form.is_valid():
            data = form.cleaned_data
            profile.display_name = data['display_name']
            profile.profile_pic = data['profile_pic']
            profile.dob = data['dob']
            profile.phone = data['phone']
            profile.bio = data['bio']
            form.save()
            return HttpResponseRedirect(f"/profile/{profile.id}/")

    form = ProfileEdditForm(initial=initial)
    context.update({'form': form})

    return render(request, "profileform.html", {'form': form})


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
