from django.urls import path

from api.views import (
    ImageList,
    image_upload,
)

app_name = "api"

urlpatterns = [
    path("images/", ImageList.as_view(), name="image-list"),
    path("images/upload/", image_upload, name="image-upload"),
]
