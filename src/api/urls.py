from django.urls import path, include

from api.views import (
    PostViewSet,
    ImageViewSet,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
