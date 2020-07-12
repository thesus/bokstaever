from django.urls import path

from frontend.views import (
    IndexView,
    PostView,
    PageView,
)


app_name = "frontend"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>", PostView.as_view(), name="post-detail"),
    path("<slug:slug>", PageView.as_view(), name="page-detail"),
]
