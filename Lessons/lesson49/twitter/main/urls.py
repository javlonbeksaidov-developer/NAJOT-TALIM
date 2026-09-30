from django.urls import path

from .views import *

app_name = "twits"

urlpatterns = [
    path("profiles/", profiles_list, name="profiles_app")
]