from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.all_posts, name="all-posts"),
    path("posts/<slug:slug>", views.specific_post, name="specific-post"), # /posts/2021-jan-1-awesome-day
    path("posts/<int:post_id>", views.specific_post_by_id, name="specific-post-by-id"), # /posts/3412

]
