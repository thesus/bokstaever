from django import template
from random import randint

register = template.Library()

@register.simple_tag
def random_color():
    colors = ['#d12229', '#00a499', '#ffc72c', '#28335c']
    number = randint(0, (len(colors) - 1))
    return colors[number]
