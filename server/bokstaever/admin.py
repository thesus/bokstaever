from django.contrib import admin

from bokstaever.models import (
    Image,
    Post,
    DatabasePage,
    FilePage,
    Settings
)


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['thumbnail']


class FilePageAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', 'headline', 'path']


admin.site.register(Image, ImageAdmin)
admin.site.register(FilePage, FilePageAdmin)
admin.site.register(DatabasePage)
admin.site.register(Post)
admin.site.register(Settings)
