from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    context = {
        'posts': posts
    }
    return render(request, 'core/frontpage.html', context=context)

def about(request):
    return render(request, 'core/about.html')

def robot_txt(request):
    text = [
        "User-Agent: *",
        "Dissallow: /admin/",
    ]
    
    return HttpResponse("\n".join(text), content_type="text/plain")