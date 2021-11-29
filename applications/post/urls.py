from django.urls import path
from applications.post.views import CategoryListView,  PostDetailView , PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('categories-list/', CategoryListView.as_view()),
    path('post-detail/<int:pk>/', PostDetailView.as_view()),
    path('post-list/', PostListView.as_view()),
    path('post-create/', PostCreateView.as_view()),
    path('post-update/<int:pk>/', PostUpdateView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
]
