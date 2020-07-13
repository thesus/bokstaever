from django.conf import settings
from bokstaever.models import PageModel


def info(request):
    return {
        "sitemap": PageModel.objects.filter(show_menu=True)
        .order_by("headline")
        .values_list("headline", "slug"),
    }
