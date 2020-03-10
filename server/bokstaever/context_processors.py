from django.conf import settings
from bokstaever.models import PageModel


def info(request):
    return {
        "settings": {
            "size": settings.PAGE_SIZE,
            "title": settings.APPLICATION_TITLE,
        },
        "sitemap": PageModel.objects.filter(show_menu=True)
        .order_by("headline")
        .values_list("headline", "slug"),
    }
