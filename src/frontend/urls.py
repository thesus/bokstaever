from django.urls import path
from django.conf import settings

from frontend.views import (
    IndexView,
    PostView,
    PageView,
)


app_name = "frontend"

urlpatterns = []

# Include a image page if the feed is enabled under the specified path
# This is included first in order to allow overriding other pages
if settings.INCLUDE_IMAGE_FEED:
    from frontend.views import ImageView  # noqa

    urlpatterns += [
        path(settings.IMAGE_FEED_PATH, ImageView.as_view(), name="image-list")
    ]

urlpatterns += [
    path("", IndexView.as_view(), name="index"),
    path("<slug:slug>", PageView.as_view(), name="page-detail"),
    path("posts/<int:pk>", PostView.as_view(), name="post-detail"),
]
