from django.contrib import admin

from bokstaever.models import Post, DatabasePage, FilePage, Settings

from images.models import Image


class FilePageAdmin(admin.ModelAdmin):
    readonly_fields = ["slug", "headline", "path"]


admin.site.register(Image)
admin.site.register(FilePage, FilePageAdmin)
admin.site.register(DatabasePage)
admin.site.register(Post)
admin.site.register(Settings)
