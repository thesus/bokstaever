from django.db import models

class Image(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )

    def __str__(self):
        return '{0.title}'.format(self)


class File(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )

    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    path = models.ImageField(
        upload_to='upload',
        height_field='height',
        width_field='width'
    )

    def __str__(self):
        return '{0.image.title} - {0.height} x {0.width}'.format(
            self
        )
