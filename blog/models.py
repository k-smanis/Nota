from django.db import models
from django.utils.text import slugify


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=20)
    email = models.EmailField(null=True)

    def __str__(self):
        name_parts = [self.first_name, self.middle_name, self.last_name]
        return " ".join(p for p in name_parts if p)


class TagModel(models.Model):
    tag_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.tag_name)


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField()
    content = models.TextField()  # * markdown content
    image = models.ImageField(upload_to="post_images")
    author = models.ForeignKey(
        to=AuthorModel, on_delete=models.SET_NULL, related_name="posts", null=True
    )
    date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(to=TagModel, related_name="posts")

    def save(self, *args, **kwargs) -> None:
        if not self.slug:  #! Prevents Slug Collisions
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-date"]
