from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from images.models import Image


class Gallery(models.Model):
    """Includes one or more images and a unique name."""

    name = models.CharField(max_length=50, unique=True, verbose_name=_("Name"))
    images = models.ManyToManyField(Image, verbose_name=_("Images"))


TEXT_CHOICES = (
    ("md", _("Markdown")),
    ("mdhtml", _("Markdown with inline HTML")),
    ("html", _("HTML")),
    ("raw", _("Raw, linebreaks are rendered")),
)


class SiteModel(models.Model):
    """Abstract model for all posts and pages."""

    image = models.ForeignKey(
        Image, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Image")
    )

    text = models.TextField(verbose_name=_("Text"))
    type = models.CharField(
        max_length=6, choices=TEXT_CHOICES, default="md", verbose_name=_("Typ")
    )

    def __str__(self):
        return f"{self.headline}"

    class Meta:
        abstract = True


class Post(SiteModel):
    """Blog style articles with editors and drafts."""

    published = models.DateField(auto_now_add=True, verbose_name=_("Published"))
    editors = models.ManyToManyField(User, verbose_name=_("Editors"))
    headline = models.CharField(max_length=200, verbose_name=_("Headline"))
    draft = models.BooleanField(default=False, verbose_name=_("Draft"))

    class Meta:
        ordering = ["-published", "-pk"]


class PageManager(models.Manager):
    def get_by_natural_key(self, slug):
        return self.get(slug=slug)


class PageModel(models.Model):
    """Wrapper around page types."""

    objects = PageManager()

    slug = models.SlugField(max_length=200, verbose_name=_("Slug"))
    headline = models.CharField(max_length=200, verbose_name=_("Headline"))
    show_menu = models.BooleanField(default=True, verbose_name=_("Show menu"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline)
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.slug,)

    def __str__(self):
        return f"{self.headline}"

    class Meta:
        unique_together = ("slug",)
        ordering = ["-pk"]


class FilePage(PageModel):
    """Page that is loaded from a file without database interaction."""

    path = models.CharField(max_length=200, verbose_name=_("Path"))


class DatabasePage(PageModel, SiteModel):
    """Normal page that get's the content from the database."""

    pass
