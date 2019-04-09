from django.db import models

from django.utils.text import slugify

from django.contrib.auth.models import User

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
    """Contains in a scaled down version and a thumbnail."""
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
                resize(self.image, 1800),
                save=False
            )
            self.thumbnail.save(
                '{0}.png'.format(self.title),
                resize(self.image, 500),
                save=False
            )
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return '{0.title}'.format(self)

    class Meta:
        ordering = ['-pk', ]


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

    # Longer information featured on the index page.
    description = models.TextField(blank=True)

    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    # Default page size for paginated views in the frontend part
    pagesize = models.PositiveSmallIntegerField(
        default=4
    )
