from django.contrib import admin
from .models import TagModel, AuthorModel, PostModel


# Admin Configuartions
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["tag_name"]
    search_fields = ["tag_name"]


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["user_name", "first_name", "middle_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "user_name"]
    ordering = ["last_name", "first_name"]


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date"]
    list_filter = ["author", "date", "tags"]
    search_fields = ["title", "excerpt", "content"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags"]  # makes tag selection easier in the form
    autocomplete_fields = ["author"]


# Register your models here.
admin.site.register(TagModel, TagModelAdmin)
admin.site.register(AuthorModel, AuthorModelAdmin)
admin.site.register(PostModel, PostModelAdmin)
