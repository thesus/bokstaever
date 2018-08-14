from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User

from django.urls import reverse

from bokstaever.images import resize


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


TEXT_CHOICES = (
    ('md', 'Markdown'),
    ('mdhtml', 'Markdown with inline HTML'),
    ('html', 'HTML'),
    ('raw', 'Raw, linebreaks are rendered')
)
class SiteModel(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    text = models.TextField()
    type = models.CharField(
        max_length=6,
        choices=TEXT_CHOICES,
        default='md'
    )
    draft = models.BooleanField(default=False)

    slug = models.SlugField(max_length=200)

    def __str__(self):
        return '{0.headline}'.format(self)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Post(SiteModel):
    published = models.DateField(auto_now_add=True)
    editors = models.ManyToManyField(User)

    class Meta:
        ordering = ['-published', '-pk']


class Page(SiteModel):
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-pk']


THEME_CHOICES = (
    ('css/brevlada.css', 'brevlåda'),
    ('css/frimarke.css', 'frimärke')
)

BEHAVIOR_CHOICES = (
    ('blog', 'Blog'),
    ('site', 'Site')
)

class Settings(SingletonModel):
    name = models.CharField(max_length=200, default='My nice page')
    email = models.EmailField(blank=True)
    info = models.TextField(blank=True)
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    theme = models.CharField(
        max_length=50,
        choices=THEME_CHOICES,
        default='css/brevlada.css'
    )

    behavior = models.CharField(
        max_length=20,
        choices=BEHAVIOR_CHOICES,
        default='site'
    )
