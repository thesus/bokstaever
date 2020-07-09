from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

from django.urls import include, path

from bokstaever.views import LatestPostsFeed


app_name = "bokstaever"
template = "registration/form.html"

urlpatterns = [
    path("", include("frontend.urls", namespace="frontend")),
    path("feed/", LatestPostsFeed(), name="feed"),
    path("admin/", admin.site.urls),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
    path("api/", include("api.urls", namespace="api"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
