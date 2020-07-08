from django.urls import path

from dashboard.views import PostList, PostUpdate, PostCreate, ImageListSimple

app_name = "dashboard"

urlpatterns = [
    # path("", )
    path("posts/", PostList.as_view()),
    path("posts/<int:pk>/", PostUpdate.as_view(), name="post-edit"),
    path("posts/create", PostCreate.as_view()),
    path("images/simple/", ImageListSimple.as_view()),
]
