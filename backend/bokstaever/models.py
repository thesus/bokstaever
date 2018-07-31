from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User

from django.urls import reverse

from bokstaever.images import resize


class Image(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )
    image = models.ImageField(
        upload_to='upload',
    )
    thumbnail = models.ImageField(
        upload_to='thumnails',
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.image.save(
                '{0}.png'.format(self.title),
                resize(self.image, 1600),
                save=False
            )
            self.thumbnail.save(
                '{0}.png'.format(self.title),
                resize(self.image, 400),
                save=False
            )
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return '{0.title}'.format(self)

    class Meta:
        ordering = ['-pk', ]

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

    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-published', '-pk']


class Page(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=200)

    text = models.TextField()

    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-pk']


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Settings(SingletonModel):
    name = models.CharField(max_length=200, default='My nice page')
    email = models.EmailField(blank=True)
    info = models.TextField(blank=True)
