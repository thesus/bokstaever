from django.forms import Field
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from dashboard.widgets import ImageSelect
from bokstaever.models import Image

class ImageChoiceField(Field):
    widget = ImageSelect

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

    def clean(self, value):
        try:
            return Image.objects.get(pk=value)
        except ObjectDoesNotExist:
            if self.is_required:
                raise ValidationError(_("The given image does not exist."))
            else:
                return None

