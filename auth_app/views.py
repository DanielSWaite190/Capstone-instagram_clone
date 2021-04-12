from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from instaUser_app.models import Profile
from auth_app.forms import Login_form, SignupForm

def login_view(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Profile = authenticate(
                request,
                username=data["username"],
                password=data["password"]
            )
            if Profile:
                login(request, Profile)
                return HttpResponseRedirect(request.GET.get("next", reverse("home_feed")))

    form = Login_form()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_feed"))

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = Profile.objects.create_user(
                    username=data['username'],
                    password=data['password'],
                    email=data['email'],
                    display_name=data['display_name'],
                    dob=data['dob'],
                    # phone=data['phone']

                )
            login(request, new_user)

            return HttpResponseRedirect(reverse("home_feed"))


    form = SignupForm()
    return render(request, "form.html", {'form': form, 'title': 'SignUp'})

# @login_required
# def deleteuser_view(request, username):
#     try:
#         Delete = Profile.objects.get(username = username)
#         Delete.delete()
#         messages.success(request, "Profile Successfully Deleted!!")
