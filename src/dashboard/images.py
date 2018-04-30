from PIL import Image as IMG

from io import BytesIO

from bokstaever.models import (
    Image,
    File
)

from django.core.files.base import ContentFile


def get_image_height(width, height, desired_width):
    percent = desired_width / width
    return (height * percent)


def crop_image(image, width):
    return image.resize(
        (
            int(width),
            int(get_image_height(
                image.size[0],
                image.size[1],
                width
            ))
        )
    )


def save_image(image, title):
    instance = Image.objects.create(title=title)

    original = IMG.open(image)

    image_sizes = (1200, 900, 400)
    for size in image_sizes:
        with BytesIO() as f:
            crop_image(original, size).save(f, format='png')

            resized = File()
            resized.image = instance
            resized.path.save(
                '{0}_{1}.png'.format(instance.title, size),
                ContentFile(f.getvalue())
            )
