from django.urls import path, include

from api.views import (
    PostViewSet,
    ImageViewSet,
    SettingsUpdateView,
    PageViewSet
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('images', ImageViewSet)
router.register('pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('settings/', SettingsUpdateView.as_view())
]
