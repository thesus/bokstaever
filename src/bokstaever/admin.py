from django.contrib import admin

from bokstaever.models import (
    Image,
    File,
    Post
)

admin.site.register(Image)
admin.site.register(File)
admin.site.register(Post)
