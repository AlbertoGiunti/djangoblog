from django.shortcuts import render
from django.http import HttpResponse  # gives us the ability to return a response to the browser
from .models import Post


# Create your views here.
def home(request):
    # Dictionary
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Page"})


def new(request):
    return HttpResponse('<h1>New Page</h1>')

