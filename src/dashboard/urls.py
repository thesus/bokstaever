from django.urls import path

from dashboard.views import (
    ImageView,
    PostView
)

urlpatterns = [
    path('images/upload/', ImageView.as_view()),
    path('post/edit/', PostView.as_view()),
    path('post/edit/<int:id>', PostView.as_view())
]
