from django import forms
from .models import PostModel, CommentModel


class PostForm(forms.ModelForm):
    new_tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = PostModel
        exclude = ["slug", "tags"]
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

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        # Handle manual tag parsing
        tag_string = self.cleaned_data.get("new_tags", "")
        tag_names = [t.strip() for t in tag_string.split(",") if t.strip()]
        tags = []

        from .models import TagModel  # avoid circular import

        for name in tag_names:
            tag, _ = TagModel.objects.get_or_create(tag_name=name)
            tags.append(tag)

        post.tags.set(tags)

        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["content", "user_name", "user_email"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "content": "Your Comment",
        }
