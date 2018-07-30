from django.contrib import admin

from bokstaever.models import (
    Image,
    Post,
    Settings
)

class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['thumbnail']

admin.site.register(Image, ImageAdmin)
admin.site.register(Post)
admin.site.register(Settings)
