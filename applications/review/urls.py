from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
# from django.urls import path

from applications.review.views import ReviewViewSet #, WhoLikeListView

router = DefaultRouter()
router.register('review', ReviewViewSet)

urlpatterns = [
    # path('wholike-list', WhoLikeListView.as_view()),
]

urlpatterns.extend(router.urls)
