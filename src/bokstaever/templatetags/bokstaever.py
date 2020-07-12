from django import template

import markdown
import math
import os

from django.conf import settings
from django.utils.safestring import mark_safe

from .extensions import EscapeHTMLExtension, GalleryExtension, ImageExtension


register = template.Library()


@register.filter()
def markdownify(text, html_escape=True):
    extensions = [
        "markdown.extensions.extra",
        "markdown.extensions.nl2br",
        GalleryExtension(),
        ImageExtension(),
    ]

    extensions += [EscapeHTMLExtension(),] if html_escape else []

    html = markdown.markdown(text, extensions=extensions)
    return mark_safe(html)


@register.filter()
def readtime(text):
    words = len(text.split())
    seconds = math.ceil(words / 265)
    return seconds if seconds > 1 else 1


@register.filter()
def get_range(value):
    return range(value)


@register.simple_tag()
def svg(filename):
    for directory in settings.STATICFILES_DIRS:
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            break
        else:
            path = None

    if not path:
        return mark_safe("svg {} not found!".format(filename))

    path = os.path.join(settings.STATICFILES_DIRS[0], filename)
    with open(path) as f:
        svg = mark_safe(f.read())
    return svg
