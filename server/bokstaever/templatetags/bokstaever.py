from django import template

import markdown

from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def markdownify(text):
    html = markdown.markdown(text, extensions=['markdown.extensions.extra',])
    return mark_safe(html)
