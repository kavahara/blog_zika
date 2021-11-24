from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='Authentication API',
        default_version='v1',
        description='test description',
    ),
    public=True,
)

urlpatterns = [
    path('', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('auth/', include('applications.account.urls')),
    path('posts/', include('applications.posts.urls')),
    path('review/', include('applications.review.urls')),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)