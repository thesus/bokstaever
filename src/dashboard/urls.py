from django.urls import path

from dashboard.views import (
    ImageCreate,
    PostCreate,
    PostUpdate
)

app_name = 'dashboard'

urlpatterns = [
    path('images/upload/', ImageCreate.as_view(), name='image-create'),
    path('post/edit/', PostCreate.as_view(), name='post-create'),
    path('post/edit/<int:pk>', PostUpdate.as_view(), name='post-edit')
]
