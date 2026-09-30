from django.http import HttpResponse
from django.shortcuts import render

from .models import Profiles

# Create your views here.

def profiles_list(request):
    profiles = Profiles.objects.all()

    javlon = Profiles.objects.get(user_id = 1)

    print(javlon)

    javlon.bio = "Bio has updated"
    javlon.save()

    return HttpResponse(content=f"Succes {profiles}")