from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

from bokstaever.views import (
    PostListView,
    PostDetailView
)

app_name = 'bokstaever'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    path('', PostListView.as_view()),
    path('<int:page>', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
