from django.contrib import admin

from applications.posts.models import Posts, PostsImage


class InlinePostsImage(admin.TabularInline):
    model = PostsImage
    extra = 1
    fields = ['image', ]


class PostsAdminDisplay(admin.ModelAdmin):
    inlines = [InlinePostsImage, ]


admin.site.register(Posts, PostsAdminDisplay)