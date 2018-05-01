from django import forms

from bokstaever.models import Post

class ImageForm(forms.Form):
    image = forms.ImageField()
    # title = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['headline', 'text']

