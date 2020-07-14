from django import forms
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from bokstaever.models import (
    Post,
    DatabasePage,
    Image,
    Gallery,
)

from dashboard.fields import ImageChoiceField


class PostForm(forms.ModelForm):
    image = ImageChoiceField(required=False, label=_("Image"))

    class Meta:
        model = Post
        fields = ["headline", "draft", "text", "type", "image"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["title", "feed"] if settings.INCLUDE_IMAGE_FEED else ["title"]

class PageForm(forms.ModelForm):
    image = ImageChoiceField(required=False, label=_("Image"))

    class Meta:
        model = DatabasePage
        fields = ["headline", "show_menu", "text", "type", "image"]


class GalleryForm(forms.ModelForm):
    images = ImageChoiceField(multiple=True, label=_("Images"))

    class Meta:
        model = Gallery
        fields = ["name", "images"]
