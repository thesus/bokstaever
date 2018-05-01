from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User


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


class Post(models.Model):
    headline = models.CharField(max_length=200)

    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    text = models.TextField()

    published = models.DateField(auto_now_add=True)
    draft = models.BooleanField(default=False)

    editors = models.ManyToManyField(User)

    url_slug = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.url_slug:
            self.url_slug = slugify(self.headline)
        super().save(*args, **kwargs)


class Settings(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Settings, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.object.get()
        except cls.DoesNotExist:
            return cls()
