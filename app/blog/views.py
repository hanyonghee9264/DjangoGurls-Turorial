import os
import random

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Post


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
