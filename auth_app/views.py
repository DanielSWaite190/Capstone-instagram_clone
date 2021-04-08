from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from instaUser_app.models import Profile
from auth_app.forms import Login_form


def login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Profile = authenticate(
                request,
                username=data["username"],
                email=data["email"],
                password=data["password"]
            )
            if Profile:
                login(request, Profile)
                return HttpResponseRedirect(request.GET.get("next", reverse("home_feed")))

    form = Login_form()
    return render(request, "auth_app/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_feed"))
