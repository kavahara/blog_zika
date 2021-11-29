from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework import generics

from applications.review.models import Review, Like
from applications.review.permissions import IsReviewAuthor
from applications.review.serializers import ReviewSerializer#, WhoLikeSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated, ]
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        elif self.action == 'like':
            permissions = [IsAuthenticated, ]
        else:
            permissions = [IsReviewAuthor, ]
        return [permission() for permission in permissions]


    @action(detail=True, methods=['POST'])
    def Like(self, request, *args, **kwargs):
        review = self.get_object()
        like_obj, _ = Like.objects.get_or_create(review=review, user=request.user)
        like_obj.like = not like_obj.like
        like_obj.save()
        status = 'liked'
        if not like_obj.like:
            status = 'unlike'
        return Response({'status': status})

    def get_serializer_context(self):
        return {'request': self.request}


# class WhoLikeListView(generics.ListAPIView):
#     queryset = Like.objects.all()
#     serializer_class = WhoLikeSerializer
