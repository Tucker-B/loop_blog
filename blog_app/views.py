from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
# Create your views here.

# posts [
# ]

def index(req):
    try:
        return render(req, "blog_app/index.html")
    except:
        raise Http404("Something went wrong")

def all_posts(req):
    try:
        return render(req, "blog_app/all-posts.html")
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