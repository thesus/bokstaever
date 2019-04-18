from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from images.models import Image

class SingletonModel(models.Model):
    """Ensures that only one instance of a Model exists."""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Gallery(models.Model):
    """Includes one or more images and a unique name."""
    name = models.CharField(max_length=50, unique=True)

    images = models.ManyToManyField(
        Image
    )


TEXT_CHOICES = (
    ('md', 'Markdown'),
    ('mdhtml', 'Markdown with inline HTML'),
    ('html', 'HTML'),
    ('raw', 'Raw, linebreaks are rendered')
)


class SiteModel(models.Model):
    """Abstract model for all posts and pages."""

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

    def __str__(self):
        return '{0.headline}'.format(self)

    class Meta:
        abstract = True


class Post(SiteModel):
    published = models.DateField(auto_now_add=True)
    editors = models.ManyToManyField(User)
    headline = models.CharField(max_length=200)

    class Meta:
        ordering = ['-published', '-pk']


class PageManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class PageModel(models.Model):
    """Wrapper around page types."""
    objects = PageManager()

    slug = models.SlugField(max_length=200)
    headline = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.slug,)

    def __str__(self):
        return '{0.headline}'.format(self)

    class Meta:
        unique_together = ('slug', )
        ordering = ['-pk']


class FilePage(PageModel):
    """Page that is loaded from a file without database interaction."""
    path = models.CharField(max_length=200)


class DatabasePage(PageModel, SiteModel):
    """Normal page that get's the content from the database."""
    pass


class Settings(SingletonModel):
    """Model with only one instance. Stores application wide settings."""
    name = models.CharField(max_length=200, default='My nice page')
    email = models.EmailField(blank=True)

    # Short info used in footer
    info = models.TextField(blank=True)

    # Default page size for paginatated index page
    pagesize = models.PositiveSmallIntegerField(
        default=4
    )
