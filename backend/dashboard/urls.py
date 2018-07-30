from django.urls import path

from django.views.generic import TemplateView

app_name = 'dashboard'

urlpatterns = []
pages = {
    'image-upload': (
        'images/edit/',
        'dashboard/image/edit.html'
    ),
    'image-list': (
        'images/list/',
        'dashboard/image/list.html'
    ),
    'post-create': (
        'posts/edit/',
        'dashboard/post/edit.html'
    ),
    'post-edit':(
        'posts/edit/<int:pk>',
        'dashboard/post/edit.html'
    ),
    'post-list': (
        'posts/list/',
        'dashboard/post/list.html'
    ),
    'index': (
        '',
        'dashboard/index.html'
    ),
    'settings-edit': (
        'settings/edit/',
        'dashboard/settings.html'
    )
}

for k, v in pages.items():
    urlpatterns.append(
        path(v[0], TemplateView.as_view(template_name=v[1]), name=k)
    )
