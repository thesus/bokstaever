from django import forms

from dashboard.images import save_image


class ImageForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()

    def create_images(self):
        self.pk = save_image(
            self.cleaned_data['image'],
            self.cleaned_data['title']
        )
