from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

app_name = 'bokstaever'

template = 'registration/form.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    path('api/auth/', include('djoser.urls.jwt')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
