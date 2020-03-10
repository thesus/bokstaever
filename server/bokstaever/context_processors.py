from bokstaever.models import Settings, PageModel


def info(request):
    return {
        "settings": Settings.load(),
        "sitemap": PageModel.objects.filter(show_menu=True)
        .order_by("headline")
        .values_list("headline", "slug"),
    }
