from django import forms
from .models import PostModel


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ["slug"]
        error_messages = {
            "image": {"required": "Don't forget to add an image — visuals matter."},
            "author": {"required": "Please tell us who wrote this post."},
            "date": {"required": "When was this written? Date is missing."},
            "title": {"required": "Every post needs a title — give it one."},
            "excerpt": {"required": "Add a short summary to hook the reader."},
            "content": {"required": "You need to write something. Right?"},
        }
        widgets = {
            "excerpt": forms.Textarea(),
            "content": forms.Textarea(),
            "tags": forms.SelectMultiple(attrs={"size": 5}),
        }
