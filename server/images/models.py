import errno
import os
import uuid

from django.conf import settings
from django.db import models
import django_rq

from images.utils import process


class ImageFile(models.Model):
    """Stores an image on a specific location and it's dimensions."""
    image_file = models.FileField()
    height = models.IntegerField()
    width = models.IntegerField()


class Image(models.Model):
    """Stores multiple versions of a image in different sizes."""
    title = models.CharField(max_length=200)
    files = models.ManyToManyField(ImageFile)

    def save(self, *args, **kwargs):
        print(kwargs)
        image = kwargs.pop('image', None)

        # super().save(*args, **kwargs)
        if image:
            self.store(image)

    def store(self, image):
        # Take filename from last dot and name it after an id
        name = "{0}.{1}".format(
            uuid.uuid4(),
            image.name.split(".")[-1]
        )

        try:
            os.makedirs(settings.IMAGE_ROOT)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        fullpath = os.path.join(settings.IMAGE_ROOT, name)
        with open(fullpath, 'wb') as f:
            for c in image.chunks():
                f.write(c)

        queue = django_rq.get_queue('default')
        queue.enqueue(
            process,
            classes=(Image, ImageFile),
            pk=self.pk,
            filename=name
        )
