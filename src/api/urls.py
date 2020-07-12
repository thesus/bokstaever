from django.urls import path

from api.views import (
    ImageList,
    ImageCreate,
)

app_name = "api"

urlpatterns = [
    path("images/", ImageList.as_view(), name="image-list"),
    path("images/upload/", ImageCreate.as_view(), name="image-upload"),
]
