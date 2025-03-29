from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .forms import CommentForm
import markdown

from .models import PostModel, CommentModel
from .forms import PostForm


# Create your views here.


def blog_index(request) -> HttpResponse:
    """
    Renders the homepage of the blog, displaying the three most recent posts.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response containing the latest three blog posts.
    """
    latest_posts = PostModel.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})


def blog_list(request) -> HttpResponse:
    """
    Renders a page displaying all blog posts, ordered by most recent.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML response containing all blog posts.
    """
    posts = PostModel.objects.order_by("-date").all()
    return render(request, "blog/blog_list.html", {"posts": posts})


class BlogPostInteractView(View):
    """
    Handles the rendering and processing of a blog post along with its comments.
    Includes functionality for displaying comments and adding new ones.
    """

    def is_saved_for_later(self, request, post_id) -> bool:
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, post_slug) -> HttpResponse:
        """
        Renders the blog post page with the content and the comment form.

        Args:
            request (HttpRequest): The HTTP request object.
            post_slug (str): The slug of the blog post to display.

        Returns:
            HttpResponse: A rendered HTML response containing the blog post and comment form.
        """
        post = PostModel.objects.get(slug=post_slug)
        post.content = markdown.markdown(
            str(post.content)
        )  #! Convert Markdown to HTML for browser support of Markdown
        is_saved_for_later = self.is_saved_for_later(request, post.id)

        comment_form = CommentForm()
        comments = CommentModel.objects.filter(post__slug=post_slug).order_by("-id")
        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
                "is_saved_for_later": is_saved_for_later,
            },
        )

    def post(self, request, post_slug) -> HttpResponse:
        """
        Handles the submission of a comment form, validates the input, and saves the comment.

        If the form is valid, the comment is saved and the user is redirected back to the post page.
        If invalid, the page is re-rendered with errors.

        Args:
            request (HttpRequest): The HTTP request object containing the comment data.
            post_slug (str): The slug of the blog post where the comment is to be added.

        Returns:
            HttpResponse: A redirected or re-rendered response depending on the form validation.
        """
        submitted_comment_form = CommentForm(request.POST)
        relevant_post_model = PostModel.objects.get(slug=post_slug)

        if submitted_comment_form.is_valid():
            submitted_comment_model = submitted_comment_form.save(commit=False)
            submitted_comment_model.post = relevant_post_model
            submitted_comment_model.save()
            return redirect("blog_post", post_slug=post_slug)
        else:
            comments = CommentModel.objects.filter(post__slug=post_slug)
            return render(
                request,
                "blog/blog_post.html",
                {
                    "post": relevant_post_model,
                    "comments": comments,
                    "comment_form": submitted_comment_form,
                },
            )


class BlogPostCreateView(View):
    """
    Handles the rendering and processing of the form for creating new blog posts.
    """

    def get(self, request) -> HttpResponse:
        """
        Renders the form for creating a new blog post.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response containing the post creation form.
        """
        post_form = PostForm()
        return render(request, "blog/blog_post_form.html", {"post_form": post_form})

    def post(self, request) -> HttpResponse:
        """
        Handles the submission of a new blog post creation form.

        If the form is valid, the new post is saved, and the user is redirected to the blog list.
        If invalid, the page is re-rendered with the form errors.

        Args:
            request (HttpRequest): The HTTP request object containing the blog post data.

        Returns:
            HttpResponse: A redirected or re-rendered response depending on the form validation.
        """
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse("blog_list"))
        else:
            return render(request, "blog/blog_post_form.html", {"post_form": post_form})


class ReadLaterView(View):
    """
    Handles the functionality for storing posts to be read later.
    The `get` method renders the stored posts, and the `post` method allows
    the user to add a post to the "Read Later" list in the session.
    """

    def get(self, request):
        """
        Retrieves the list of stored posts from the session and renders the stored posts page.

        If there are posts saved for reading later, they will be displayed.
        If no posts are stored, a message will inform the user that they have no saved posts.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A rendered HTML response containing either the list of
                          stored posts or a message informing the user there are no posts saved.
        """
        stored_posts_ids = request.session.get("stored_posts")
        template_context = {}

        if stored_posts_ids and len(stored_posts_ids) > 0:
            template_context["stored_posts"] = PostModel.objects.filter(
                id__in=stored_posts_ids
            )
            template_context["has_posts"] = True
        else:
            template_context["stored_posts"] = []
            template_context["has_posts"] = False

        return render(
            request, "blog/blog_stored_posts.html", {"context": template_context}
        )

    def post(self, request):
        """
        Handles the POST request to store a blog post in the "Read Later" list.
        Adds the post ID to the session to track which posts the user wants to read later.

        If the post is already in the "Read Later" list, it will not be added again.
        After adding the post to the session, the user is redirected to the blog index page.

        Args:
            request (HttpRequest): The HTTP request object containing the post data,
                                   including the post ID to be saved.

        Returns:
            HttpResponse: A redirect to the blog index page after the post is saved.
        """
        stored_posts = request.session.get("stored_posts")

        # Initialize Session for First Post
        if stored_posts is None:
            stored_posts = []

        # Handle Posts (Store unstored posts OR Unstore stored posts)
        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts

        return redirect(reverse("blog_index"))
