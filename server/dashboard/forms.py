from django import forms

from bokstaever.models import (
        Post,
        DatabasePage
)

from dashboard.fields import ImageChoiceField

class PostForm(forms.ModelForm):
    image = ImageChoiceField()

    class Meta:
        model = Post
        fields = ["headline", "draft", "text", "type", "image"]


class PageForm(forms.ModelForm):
    image = ImageChoiceField()

    class Meta:
        model = DatabasePage
        fields = ["headline", "show_menu", "text", "type", "draft", "image"]

class ImageForm(forms.Form):
    image = forms.FileField()
    title = forms.CharField()
