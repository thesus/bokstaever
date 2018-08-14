from django import template

import markdown
import math

from django.utils.safestring import mark_safe

register = template.Library()

class EscapeHTML(markdown.extensions.Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']

@register.filter()
def markdownify(text, html_escape=True):
    extensions = ['markdown.extensions.extra', ]
    extensions += [EscapeHTML()] if html_escape else []

    html = markdown.markdown(text, extensions=extensions)
    return mark_safe(html)


@register.filter()
def readtime(text):
    words = len(text.split())
    seconds = math.ceil(words / 265)
    return seconds if seconds > 1 else 1
