from django import template
from random import randint

register = template.Library()

@register.filter
def estimate_time(text):
    words = len(text.split())
    minutes = int(round(words / 180))
    time_string = minutes if minutes >= 1 else 1
    return '{} min'.format(time_string)
