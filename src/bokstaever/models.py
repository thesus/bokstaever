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

    def path(self):
        return '{0}'.format(self.files.first().path.url)

    def __str__(self):
        return '{0.title}'.format(self)


class File(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name='files'
    image = models.ImageField(
        upload_to='upload'
    )

    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    path = models.ImageField(
        upload_to='upload',
        height_field='height',
        width_field='width'
    thumbnail = models.ImageField(
        upload_to='thumnails'
    )

    def save(self):
        if self.image:
            self.image.path.save(
                '{0}.png'.format(self.title),
                resize(self.image, 1600)
            )
            self.thumbnail.path.save(
                '{0}.png'.format(self.title),
                resize(self.image, 1600)
            )
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return '{0.image.title} - {0.height} x {0.width}'.format(
            self
        )
        return '{0.title}'.format(self)


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

    def get_absolute_url(self):
        return reverse('dashboard:post-edit', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-published', '-pk']


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
