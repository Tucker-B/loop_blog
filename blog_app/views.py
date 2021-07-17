from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404

from .models import Post, Tag
from .forms import PostForm

import pdb;

# Create your views here.

# posts [
# ]

def index(req):
    posts = Post.objects.order_by("-date")[:3]
    imgHostUrl = "https://loopblog-images.s3.amazonaws.com/"
    try:
        return render(req, "blog_app/index.html", {
            "posts": posts,
            "imgHostUrl": imgHostUrl
        })
    except:
        raise Http404("Something went wrong")

def all_posts(req):
    posts = Post.objects.all().order_by("-date")[:10]
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
        return render(req, "blog_app/one-post.html", {
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

def add_post(req):
    if (req.method == 'POST'):
        form = PostForm(req.POST)
        
        if form.is_valid():
            tags = form.cleaned_data['tags']
            post = Post(title=form.cleaned_data['title'], 
                excerpt=form.cleaned_data['excerpt'], 
                content=form.cleaned_data['content'], 
                image_name=form.cleaned_data['image_name'])
            
            post.save()

            for tag in tags:
                post.tags.add(tag)
            
            print(form.cleaned_data)
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    try:
        return render(req, "blog_app/add-post.html", {
            "form": form
        })
    except:
        raise Http404("Something went wrong") 