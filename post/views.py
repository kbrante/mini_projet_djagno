# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from .forms import PostForm

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

    paginator = Paginator(posts, 16) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

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

@login_required
@permission_required('post.add_post')
def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post-detail", slug = post.slug)

    context = {
        "form" : form
    }

    return render(request, "post_create.html", context)

@login_required
@permission_required('post.change_post')
def post_edit(request,slug):

    post = Post.objects.get(slug=slug)
    form = PostForm(instance = post)
    if request.method == "POST":
        form = PostForm(data = request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            return redirect("post-detail", slug = post.slug)

    context = {
        "post" : post,
        "form" : form
    }

    return render(request, "post_edit.html", context)

@login_required
@user_passes_test(lambda u:u.is_superuser)
def post_delete(request, slug):
    post = Post.objects.get(slug=slug)

    post.delete()
    return redirect('post-list')
