from django.shortcuts import render
from .models import Post



def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})

def services(request):
    return render(request, 'blog/services.html', { 'title': 'Services'})

def contact(request):
    return render(request, 'blog/contact.html', { 'title': 'Contact Us'})

