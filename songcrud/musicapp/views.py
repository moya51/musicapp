
from django.shortcuts import render
from django.http import  HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Welcome to the MusicApp")

def app(request):
    return HttpResponse("Welcome to the App")