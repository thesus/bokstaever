from django import template

import markdown
import math

from django.utils.safestring import mark_safe

from .extensions import EscapeHTMLExtension, GalleryExtension


register = template.Library()


@register.filter()
def markdownify(text, html_escape=True):
    extensions = ['markdown.extensions.extra', GalleryExtension()]

    extensions += [EscapeHTMLExtension(), ] if html_escape else []

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
