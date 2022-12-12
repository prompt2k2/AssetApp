from django.shortcuts import render
from django.http import HttpResponse
from .models import Engineer, Site, UserProfile, AssetRequest


def index(request):
    return render (request, 'index.html')

def UserProfile(request):
    return render(request, 'profile.html')
