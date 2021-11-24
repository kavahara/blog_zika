# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics #, filter
from rest_framework.pagination import PageNumberPagination
# from django_filters import rest_framework
from applications.posts.models import Posts, Like
from applications.posts.serializers import PostsSerializer, PostsDetailSerializer
from rest_framework.response import Response


class PostsListView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    pagination_class = PageNumberPagination
    # filter_backends = [DjangoFilterBackend,] # filters.SearchFilter
    # filter_class = ''# здесь должна быть фильтрация но у нас ее нету так как мы её не делали
    search_fields = ['title', ]

    def get_serializer_context(self):
        return {'request': self.request}

    # @action(detail=True, methods=['POST'])
    # def Like(self, request, *args, **kwargs):
    #     review = self.get_object()
    #     like_obj, _ = Like.objects.get_or_create(review=review, user=request.user)
    #     like_obj.like = not like_obj.like
    #     like_obj.save()
    #     status = 'liked'
    #     if not like_obj.like:
    #         status = 'unlike'
    #     return Response({'status': status})


class PostsDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsDetailSerializer


