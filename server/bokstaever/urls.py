from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from django.urls import include, path

from bokstaever.views import LatestPostsFeed


app_name = 'bokstaever'
template = 'registration/form.html'

urlpatterns = [
    path('', include('frontend.urls', namespace='frontend')),
    path('feed/', LatestPostsFeed(), name='feed'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.views.generic import TemplateView  # noqa

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += [
        path(
            'dashboard/',
            TemplateView.as_view(template_name='index.html')
        ),
    ] + static(
        '/dashboard/',
        document_root=str(settings.ROOT_DIR.path('contrib'))
    )
