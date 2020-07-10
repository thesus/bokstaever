from django import forms

from bokstaever.models import (
        Post,
        DatabasePage,
        Gallery,
)

from dashboard.fields import ImageChoiceField

class PostForm(forms.ModelForm):
    image = ImageChoiceField(required=False)

    class Meta:
        model = Post
        fields = ["headline", "draft", "text", "type", "image"]


class PageForm(forms.ModelForm):
    image = ImageChoiceField(required=False)

    class Meta:
        model = DatabasePage
        fields = ["headline", "show_menu", "text", "type", "image"]

class GalleryForm(forms.ModelForm):
    images = ImageChoiceField(multiple=True)

    class Meta:
        model = Gallery
        fields = ["name", "images"]
