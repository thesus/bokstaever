from django.urls import path

from dashboard.views import (
    DashboardIndex,
    ImageCreate,
    PostCreate,
    PostUpdate,
    PostDelete,
    PostList,
    ImageList,
    SettingsUpdate
)

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardIndex.as_view(), name='dashboard-index'),
    path('images/upload/', ImageCreate.as_view(), name='image-create'),
    path('post/edit/', PostCreate.as_view(), name='post-create'),
    path('post/edit/<int:pk>', PostUpdate.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDelete.as_view(), name='post-delte'),
    path('post/list/<int:page>', PostList.as_view(), name='post-list'),
    path('images/list/<int:page>', ImageList.as_view(), name='image-list'),
    path('settings/edit', SettingsUpdate.as_view(), name='settings-edit'),
]
