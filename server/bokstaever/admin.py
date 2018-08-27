from django.contrib import admin

from bokstaever.models import (
    Image,
    Post,
    Page,
    Settings
)


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['thumbnail']


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


admin.site.register(Image, ImageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Post)
admin.site.register(Settings)
