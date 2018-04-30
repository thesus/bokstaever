from django.db import models

class Image(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )

    def __str__(self):
        return '{}.title'.format(self)


class File(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE
    )
    path = models.ImageField(upload_to='upload')

    def __str__(self):
        return '{0}.title - {1}.height_field x {0}.width_field'.format(
            self.image,
            self.path
        )
