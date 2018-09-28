import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
