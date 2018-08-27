from django.urls import path, include

from api.views import (
    PostViewSet,
    ImageViewSet,
    SettingsUpdateView,
    PageViewSet,
    GalleryViewSet
)

from rest_framework.routers import DefaultRouter


app_name = 'api'

router = DefaultRouter()

viewsets = (
    ('posts', PostViewSet),
    ('images', ImageViewSet),
    ('pages', PageViewSet),
    ('galleries', GalleryViewSet)
)

for viewset in viewsets:
    router.register(*viewset)

urlpatterns = [
    path('', include(router.urls)),
    path('settings/', SettingsUpdateView.as_view())
]
