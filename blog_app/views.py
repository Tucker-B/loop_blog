from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponseNotFound
# Create your views here.

def index(req):
    try:
        return render(req, "blog_app/index.html")
    except:
        return HttpResponseNotFound("<h1>File or directory not found</h1>")

def all_posts(req):
    return render(req, "<h1>Some text goes here </h1>")

def specific_post(req):
    return render(req, "<h1>Some text goes here </h1>")

def specific_post_by_id(req):
    return render(req, "<h1>Some text goes here </h1>")