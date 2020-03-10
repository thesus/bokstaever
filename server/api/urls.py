from django.urls import path, include


from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api.views import (
    PostViewSet,
    ImageViewSet,
    SettingsUpdateView,
    PageViewSet,
    GalleryViewSet,
    StatisticsView,
)

from rest_framework.routers import DefaultRouter


app_name = "api"

router = DefaultRouter()

viewsets = (
    ("posts", PostViewSet),
    ("images", ImageViewSet),
    ("pages", PageViewSet),
    ("galleries", GalleryViewSet),
)

for viewset in viewsets:
    router.register(*viewset)

urlpatterns = [
    path("", include(router.urls)),
    path("settings/", SettingsUpdateView.as_view()),
    path("statistics/", StatisticsView.as_view()),
    path("auth/jwt/create/", obtain_jwt_token),
    path("auth/jwt/refresh/", refresh_jwt_token),
]
