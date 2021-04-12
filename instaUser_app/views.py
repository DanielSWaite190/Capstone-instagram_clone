from django.shortcuts import render
from django.views import View

class profile_view(View):
    template_name = "profile.html"

    def get(self, request):
        return render(request, self.template_name, {'message': 'we are good'})
