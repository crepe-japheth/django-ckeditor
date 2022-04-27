from django.shortcuts import render
from .models import (
    Post,
    Comment,
)

# Create your views here.

def index(request):
    articles = Post.objects.all()
    context = {'articles':articles}
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    article = Post.objects.get(slug=slug)
    #comment = Comment.objects.filter()
    print(article)
    print(article.body)
    context = {'article':article}
    return render(request, 'blog/detail.html', context)