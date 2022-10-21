from django.urls import path

from .views import index

urlpatterns = [
   path("musicapp/", index, name="index")
]


