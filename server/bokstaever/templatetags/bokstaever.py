from django import template

import markdown
import math

from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def markdownify(text):
    html = markdown.markdown(text, extensions=['markdown.extensions.extra',])
    return mark_safe(html)


@register.filter()
def readtime(text):
    words = len(text.split())
    seconds = math.ceil(words / 265)
    return seconds if seconds > 1 else 1
