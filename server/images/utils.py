import os.path
import PIL.Image
import PIL.ImageOps

from io import BytesIO
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.base import ContentFile


def resize(pk, filename, name, dimensions, file_class):
    fullpath = os.path.join(settings.IMAGE_ROOT, filename)
    image = PIL.Image.open(fullpath)

    orig_width, orig_height = image.size

    fit = False
    if ('w' in dimensions) and ('h' in dimensions):
        h = dimensions['h']
        w = dimensions['w']
        fit = True
    elif ('w' in dimensions):
        w = dimensions['w']
        h = (float(w) / orig_width) * orig_height
    elif ('h' in dimensions):
        h = dimensions['h']
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
            image = image.resize(
                (w, h),
                PIL.Image.LANCZOS,
            )

        # Convert to remove possible alpha channel
        image = image.convert("RGB")
        image.save(f, format='jpeg')

        instance.image_file.save(
            '{0}_{1}.jpg'.format(pk, name),
            ContentFile(f.getvalue()),
            save=False,
        )

        instance.save()

    return instance


def save_on_container(
        image_class,
        pk,
        instance,
        thumbnail=False
        ):
    container = image_class.objects.get(pk=pk)
    if thumbnail:
        container.thumbnail = instance
        container.save()
    else:
        container.files.add(instance)


def process(classes, pk, filename):
    # Generate thumbnail
    save_on_container(
        classes[0],
        pk,
        resize(
            pk,
            filename,
            'thumbnail',
            {'h': 200, 'w': 200},
            classes[1]
        ),
        thumbnail=True
    )

    for (k, v) in settings.IMAGE_SIZES.items():
        save_on_container(
            classes[0],
            pk,
            resize(pk, filename, k, v, classes[1])
        )
