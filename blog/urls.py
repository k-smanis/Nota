from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("posts/", views.blog_list, name="blog_list"),
    path(
        "posts/<slug:post_slug>", views.BlogPostInteractView.as_view(), name="blog_post"
    ),
    path(
        "comment/<slug:post_slug>/",
        views.BlogPostInteractView.as_view(),
        name="blog_comment_form",
    ),
    path("post-form/", views.BlogPostCreateView.as_view(), name="blog_post_form"),
    path("read-later/", views.ReadLaterView.as_view(), name="read_later"),
]
