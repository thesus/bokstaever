from django.forms import Field
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext as _

from dashboard.widgets import ImageSelect
from bokstaever.models import Image

class ImageChoiceField(Field):
    widget = ImageSelect

    def __init__(self, *args, multiple=False, **kwargs):
        self.multiple = multiple
        super().__init__(**kwargs)

        self.widget.multiple = multiple

    def clean(self, value):
        if not value and not self.required:
            return None
        elif not value:
            raise ValidationError(_("The field is required."))

        try:
            if self.multiple:
                id_list = [int(image) for image in value.split(",")]

                return Image.objects.filter(pk__in=id_list)
            else:
                return Image.objects.get(pk=value)
        except ObjectDoesNotExist:
            if self.required:
                raise ValidationError(_("The given image does not exist."))
            else:
                return None

