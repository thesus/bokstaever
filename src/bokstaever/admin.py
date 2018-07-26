from django.contrib import admin

from bokstaever.models import (
    Image,
    Post,
    Settings
)

admin.site.register(Image)
admin.site.register(Post)
admin.site.register(Settings)
