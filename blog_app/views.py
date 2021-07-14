from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from .models import Post, Tag

# Create your views here.

# posts [
# ]

def index(req):
    posts = Post.objects.all().order_by("date")
    try:
        return render(req, "blog_app/index.html", {
            "posts": posts
        })
    except:
        raise Http404("Something went wrong")

def all_posts(req):
    posts = Post.objects.all().order_by("date")
    try:
        return render(req, "blog_app/all-posts.html", {
            "posts": posts
        })
    except:
        raise Http404("Something went wrong")

def specific_post(req, slug):
    try:
        return render(req, "blog_app/specific-post.html")
    except:
        raise Http404("Something went wrong")

def specific_post_by_id(req, post_id):
    try:
        return render(req, "blog_app/specific-post.html")
    except:
        raise Http404("Something went wrong")