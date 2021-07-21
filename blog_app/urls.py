from django.urls import path
from django.urls.conf import re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.all_posts, name="all-posts"),
    path("posts/add", views.add_post, name="add-post"),
    path("tags/add", views.add_tag, name="add-tag"),
    re_path(r'^search/$', views.search, name="post-search"),
    path("posts/<slug:slug>", views.specific_post, name="one-post"), 
    path("posts/<slug:slug>/update", views.specific_post_update, name="update-post"),
    path("posts/<slug:slug>/delete", views.specific_post_delete, name="delete-post"),
    path("posts/<int:post_id>", views.specific_post_by_id, name="specific-post-by-id")
]
