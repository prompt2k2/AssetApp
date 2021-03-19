from django.shortcuts import render

posts = [
    {
        'author': 'Prosper PO',
        'title': 'Arsenal Related',
        'content': 'First Post Content',
        'date_posted': 'November 10, 1983'
    },
        {
        'author': 'John Doe',
        'title': 'Chelsea Related',
        'content': 'Second Post Content',
        'date_posted': 'October 12, 1992'
    }
]

def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})

def services(request):
    return render(request, 'blog/services.html', { 'title': 'Services'})

def contact(request):
    return render(request, 'blog/contact.html', { 'title': 'Contact Us'})

