from django.urls import path

from applications.posts.views import PostsListView, PostsDetailView

urlpatterns = [
    path('posts-list/', PostsListView.as_view()),
    path('posts-list/<int:pk>/', PostsDetailView.as_view()),
]