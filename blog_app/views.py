from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from .models import Post, Tag

# Create your views here.

# posts [
# ]

def index(req):
    posts = Post.objects.all().order_by("date")
    imgHostUrl = "https://loopblog-images.s3.amazonaws.com/"
    try:
        return render(req, "blog_app/index.html", {
            "posts": posts,
            "imgHostUrl": imgHostUrl
        })
    except:
        raise Http404("Something went wrong")

def all_posts(req):
    posts = Post.objects.all().order_by("date")
    imgHostUrl = "https://loopblog-images.s3.amazonaws.com/"
    try:
        return render(req, "blog_app/all-posts.html", {
            "posts": posts,
            "imgHostUrl": imgHostUrl
        })
    except:
        raise Http404("Something went wrong")

def specific_post(req, slug):
    post = Post.objects.get(slug=slug)
    imgHostUrl = f"https://loopblog-images.s3.amazonaws.com/{post.image_name}"
    try:
        return render(req, "blog_app/specific-post.html", {
            "specific_post": post,
            "imgUrl": imgHostUrl
        })
    except:
        raise Http404("Something went wrong")

def specific_post_by_id(req, post_id):
    try:
        return render(req, "blog_app/specific-post.html")
    except:
        raise Http404("Something went wrong")