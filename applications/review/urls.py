from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter

from applications.review.views import ReviewViewSet

router = DefaultRouter()
router.register('review', ReviewViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
