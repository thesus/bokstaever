from django.urls import path

from frontend.views import (
    index,
    blog,

    PostView,
    PageView
)


urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('posts/<int:pk>', PostView.as_view(), name='post-detail'),
    path('<slug:slug>', PageView.as_view(), name='page-detail')
]
