from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from instaUser_app.forms import ProfileEdditForm
from instaUser_app.models import Profile
from django.views import View
from auth_app.views import logout_view


# DSW Update
class profile_view(View):
    template_name = "profile.html"

    def get(self, request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        return render(request, self.template_name, {'profile': profile})


# DSW
@login_required
def EdditProfile_view(request, profile_id):

    # jk starts here
    context = {}
    edit = Profile.objects.get(id=profile_id)

    if request.method == "POST":
        form = ProfileEdditForm(request.POST, request.FILES)
        if form.is_valid():
            edit.profile_pic = request.FILES['profile_pic']
            data = form.cleaned_data
            edit.bio = data['bio']
            edit.display_name = data['display_name']
            edit.dob = data['dob']
            edit.save()
            return HttpResponseRedirect(reverse(
                                        'profile',
                                        args=[edit.id]))

    form = ProfileEdditForm(initial={
        'profile_pic': edit.profile_pic,
        'bio': edit.bio,
        'display_name': edit.display_name,
        'dob': edit.dob,
        })
    context.update({'form': form})
    return render(request, 'profileform.html', context)


@login_required
def assign_view(request, post_id):
    ticket = Ticket.objects.get(id=post_id)
    ticket.select_status = ('InProgress')
    ticket.assigned_to = (request.user)
    ticket.save()
    return render(request, 'assigned.html', {
        'ticket': ticket
        })
    # profile = Profile.objects.get(id=profile_id)
    # context = {}  # I might not need this
    # initial = {
    #     'display_name': profile.display_name,
    #     'profile_pic': profile.profile_pic,
    #     'dob': profile.dob,
    #     'phone': profile.phone,
    #     'bio': profile.bio
    # }

    # if request.method == "POST":
    #     form = ProfileEdditForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         profile.display_name = data['display_name']
    #         profile.profile_pic = data['profile_pic']
    #         profile.dob = data['dob']
    #         profile.phone = data['phone']
    #         profile.bio = data['bio']
    #         form.save()
    #         return HttpResponseRedirect(f"/profile/{profile.id}/")

    # form = ProfileEdditForm(initial=initial)
    # context.update({'form': form})

    # return render(request, "profileform.html", {'form': form})
    return render(request, "profileform.html", context)


# JK
@login_required()
def delete_photo_view(request, photo_id):
    prof_img = Profile.objects.get(id=photo_id).profile_pic.delete(save=True)
    return render(request, 'profile.html', {"message": "deleted successfully"})


@login_required()
def delete_user(request, user_id):
    user = Profile.objects.get(id=user_id)

    logout_view(request)
    user.delete()
    return  HttpResponseRedirect('/')


def follow(request, user_id):
    p_user = Profile.objects.get(id=user_id)
    request.user.following.add(p_user)
    return HttpResponseRedirect(f"/profile/{user_id}")


def unfollow(request, user_id):
    p_user = Profile.objects.get(id=user_id)
    request.user.following.remove(p_user)
    return HttpResponseRedirect(f"/profile/{user_id}")
