import os.path
import PIL.Image
import PIL.ImageOps

from datetime import datetime

from io import BytesIO
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.base import ContentFile


def resize(pk, filename, name, dimensions, file_class):
    image = PIL.Image.open(filename)

    orig_width, orig_height = image.size

    fit = False
    if ("w" in dimensions) and ("h" in dimensions):
        h = dimensions["h"]
        w = dimensions["w"]
        fit = True
    elif "w" in dimensions:
        w = dimensions["w"]
        h = (float(w) / orig_width) * orig_height
    elif "h" in dimensions:
        h = dimensions["h"]
        w = (float(h) / orig_height) * orig_width
    else:
        raise ImproperlyConfigured("IMAGE_SIZES contains wrong keys")

    h = int(h)
    w = int(w)
    instance = None
    with BytesIO() as f:
        instance = file_class()
        instance.height = h
        instance.width = w

        if fit:
            image = PIL.ImageOps.fit(
                image=image,
                method=PIL.Image.LANCZOS,
                size=(w, h),
                centering=(0.5, 0.5),
            )
        else:
            image = image.resize((w, h), PIL.Image.LANCZOS,)

        # Convert to remove possible alpha channel
        image = image.convert("RGB")
        image.save(f, format="jpeg", quality=95)

        instance.image_file.save(
            "{0}_{1}.jpg".format(pk, name), ContentFile(f.getvalue()), save=False,
        )

        instance.save()

    return instance


def save_on_container(image, instance, thumbnail=False):
    if thumbnail:
        image.thumbnail = instance
        image.save()
    else:
        image.files.add(instance)


def guess_and_update_date(image, filename):
    """Uses the exif date of an image to set the `creation_date`."""
    exif = PIL.Image.open(filename).getexif()
    try:
        # Exif tag for DateTimeOriginal
        date = datetime.strptime(exif[36867], "%Y:%m:%d %H:%M:%S")
        image.creation_date = date
        image.save()
    except KeyError:
        pass


def process(classes, pk, filename):
    """Process an image.

    Takes the `image.models.Image` and `image.models.ImageFile` classes
    as a first parameter in order to prevent a circular input.
    """

    image = classes[0].objects.get(pk=pk)
    filename = os.path.join(settings.IMAGE_ROOT, filename)

    guess_and_update_date(image, filename)

    # Generate thumbnail
    save_on_container(
        image,
        resize(pk, filename, "thumbnail", {"h": 600, "w": 600}, classes[1]),
        thumbnail=True,
    )

    for (k, v) in settings.IMAGE_SIZES.items():
        save_on_container(image, resize(pk, filename, k, v, classes[1]))
