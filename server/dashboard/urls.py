from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path, include

from dashboard.views import (
    Dashboard,
    PostList,
    PostUpdate,
    PostDelete,
    PostCreate,
    PageList,
    PageUpdate,
    PageDelete,
    PageCreate,
    ImageList,
    ImageUpdate,
    ImageDelete,
    ImageCreate,
    GalleryList,
    GalleryUpdate,
    GalleryDelete,
    GalleryCreate,
)

app_name = "dashboard"

urlpatterns = [
    path("", Dashboard.as_view(), name="home"),
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/<int:pk>/edit", PostUpdate.as_view(), name="post-edit"),
    path("posts/<int:pk>/delete", PostDelete.as_view(), name="post-delete"),
    path("posts/create", PostCreate.as_view(), name="post-create"),
    path("pages/", PageList.as_view(), name="page-list"),
    path("pages/<int:pk>/edit", PageUpdate.as_view(), name="page-edit"),
    path("page/<int:pk>/delete", PageDelete.as_view(), name="page-delete"),
    path("pages/create", PageCreate.as_view(), name="page-create"),
    path("images/", ImageList.as_view(), name="image-list"),
    path("images/<int:pk>/edit", ImageUpdate.as_view(), name="image-edit"),
    path("images/<int:pk>/delete", ImageDelete.as_view(), name="image-delete"),
    path("images/create", ImageCreate.as_view(), name="image-create"),
    path("galleries/", GalleryList.as_view(), name="gallery-list"),
    path("galleries/<int:pk>/edit", GalleryUpdate.as_view(), name="gallery-edit"),
    path("galleries/<int:pk>/delete", GalleryDelete.as_view(), name="gallery-delete"),
    path("galleries/create", GalleryCreate.as_view(), name="gallery-create"),

    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout",),
]
