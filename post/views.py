# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Post

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def post_list(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts
    }
    return render(request, "post_list.html", context)
