# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Post, Category

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    selected_category = None
    cat = request.GET.get("Category", None)

    if cat:
        posts = Post.objects.filter(category=cat)
        selected_category = categories.get(id=cat)
    else:
        posts = Post.objects.all()


    context = {
        "posts" : posts,
        "categories" : categories,
        "selected_category" : selected_category
    }

    return render(request, "post_list.html", context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        "post" : post
    }

    return render(request, "post_detail.html", context)
