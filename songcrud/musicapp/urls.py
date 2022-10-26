from django.urls import path

from .views import index
from .views import app

urlpatterns = [
   path("", index, name="index")
]


