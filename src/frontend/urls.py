from django.urls import path
from django.conf import settings

from frontend.views import (
    IndexView,
    PostView,
    PageView,
)


app_name = "frontend"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("<slug:slug>", PageView.as_view(), name="page-detail"),
    path("posts/<int:pk>", PostView.as_view(), name="post-detail"),
]

if settings.INCLUDE_IMAGE_PAGE:
    from frontend.views import ImageView  # noqa

    urlpatterns += [path("images/", ImageView.as_view(), name="image-list")]
