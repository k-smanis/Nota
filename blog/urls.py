from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("posts/", views.blog_list, name="blog_list"),
    path("posts/<slug:blog_slug>", views.blog_post, name="blog_post"),
]
