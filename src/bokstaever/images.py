from PIL import Image as IMG

from io import BytesIO

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

def resize(image, width):
    original = IMG.open(image)

    with BytesIO() as f:
        crop_image(original, size).save(f, format='png')
        return ContentFile(f.getvalue())
