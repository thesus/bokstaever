from django.forms.widgets import Widget

from images.models import Image

class ImageSelect(Widget):
    template_name = 'dashboard/widgets/image_select.html'

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        pk = context["widget"]["value"]

        context["url"] = Image.objects.get(pk=pk).thumbnail.image_file.url if pk else ""

        return context

