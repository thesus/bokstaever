from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

from bokstaever.views import (
    PostListView,
    PostDetailView
)

from django.contrib.auth import views as auth_views

app_name = 'bokstaever'

template = 'registration/form.html'
authentication = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name=template)),
    path('accounts/logout/', auth_views.LogoutView.as_view())
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),
    path('api/', include('api.urls'), name='api'),
    path('api/auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + authentication
