from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['author', 'title', 'created', 'updated']
    list_per_page = 15
