from django.forms.widgets import Widget

from images.models import Image

class ImageSelect(Widget):
    multiple = False
    template_name = 'dashboard/widgets/image_select.html'

    def format_value(self, value):
        return value

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        pk = context["widget"]["value"]

        if not self.multiple:
            context["url"] = Image.objects.get(pk=pk).thumbnail.image_file.url if pk else ""
        context["multiple"] = self.multiple

        return context

