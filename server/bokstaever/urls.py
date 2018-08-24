from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

from bokstaever.views import LatestPostsFeed

app_name = 'bokstaever'

template = 'registration/form.html'

urlpatterns = [
    path('', include('frontend.urls', namespace='frontend')),
    path('feed/', LatestPostsFeed(), name='feed'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
