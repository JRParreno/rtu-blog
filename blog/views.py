from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    data = {
        "posts": posts
    }
    return render(request, 'blog/home.html', data)


def about(request):
    return render(request, 'blog/about.html')
