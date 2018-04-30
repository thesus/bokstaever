from django.urls import path

from dashboard.views import ImageView

urlpatterns = [
    path('images/upload/', ImageView.as_view())
]
