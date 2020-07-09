from django.urls import path

from dashboard.views import (
    PostList,
    PostUpdate,
    PostCreate,
    PageList,
    PageUpdate,
    PageCreate,
    ImageList,
    ImageCreate,
)

app_name = "dashboard"

urlpatterns = [
    # path("", )
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostUpdate.as_view(), name="post-edit"),
    path("posts/create", PostCreate.as_view(), name="post-create"),
    path("pages/", PageList.as_view(), name="page-list"),
    path("pages/<int:pk>/", PageUpdate.as_view(), name="page-edit"),
    path("pages/create", PageCreate.as_view(), name="page-create"),
    path("images/", ImageList.as_view(), name="image-list"),
    path("images/create", ImageCreate.as_view(), name="image-create"),
]
