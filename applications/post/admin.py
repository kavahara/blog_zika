from django.contrib import admin

from applications.post.models import Category, Post

admin.site.register(Category)
admin.site.register(Post)