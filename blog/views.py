from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


posts = [
    {
        "slug": "exploring-the-appalachians",
        "image": "dummy-image-1.jpg",
        "author": "B.Hawk",
        "date": date(year=2025, month=3, day=27),
        "title": "Exploring the Appalachian Mountains: A Journey Through West Virginia",
        "excerpt": "A breathtaking hike through the Appalachian Mountains offers unparalleled views and experiences for nature enthusiasts.",
        "content": "The Appalachian Mountains in West Virginia offer some of the most beautiful hiking trails in the Eastern United States. The crisp mountain air, dense forests, and stunning vistas make it an ideal location for a nature retreat. Whether you're an experienced hiker or just looking for a weekend getaway, the trails here promise something for everyone.",
    },
    {
        "slug": "urban-gardening-tips",
        "image": "dummy-image-2.jpg",
        "author": "A.Jones",
        "date": date(year=2025, month=3, day=26),
        "title": "Urban Gardening: How to Grow Your Own Food in the City",
        "excerpt": "Urban gardening is not only possible but thriving in cities, allowing people to grow fresh produce right from their balconies.",
        "content": "Urban gardening is a growing trend, as people in cities are discovering the joys of growing their own vegetables, herbs, and even fruits in small spaces. With the right tools and techniques, anyone can start a garden, whether it's in a pot on your balcony or a vertical garden in your living room. Learn how to make the most of your space and grow fresh, healthy food right at home.",
    },
    {
        "slug": "ancient-history-of-egypt",
        "image": "dummy-image-3.jpg",
        "author": "L.Taylor",
        "date": date(year=2025, month=3, day=20),
        "title": "The Ancient History of Egypt: From Pharaohs to Pyramids",
        "excerpt": "A journey through Egypt’s fascinating history, uncovering the mysteries of the pyramids and the powerful pharaohs who ruled the land.",
        "content": "Egypt's ancient civilization is one of the most fascinating in history. From the majestic pyramids to the enigmatic Sphinx, the wonders of ancient Egypt have captivated people for centuries. The history of the pharaohs, their rise to power, and the impact they had on the world can still be felt today. This article delves into the rich history of Egypt, from the early dynasties to the grandeur of the New Kingdom.",
    },
]


def get_date(post):
    return post["date"]


# Create your views here.
def blog_index(request) -> HttpResponse:
    sorted_posts = sorted(posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"latest_posts": latest_posts})


def blog_list(request) -> HttpResponse:
    return render(request, "blog/blog_list.html", {"posts": posts})


def blog_post(request, blog_slug):
    post = next((p for p in posts if p["slug"] == blog_slug), None)
    return render(request, "blog/blog_post.html", {"post": post})
