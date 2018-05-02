from django.contrib import admin

from django.urls import include, path

from bokstaever.views import PostListView

app_name = 'bokstaever'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls'), name='dashboard'),

    path('', PostListView.as_view(), name='post-list')
]
