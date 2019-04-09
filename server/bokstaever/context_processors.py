from bokstaever.models import (
    Settings,
    PageModel
)


def info(request):
    return {
        'settings': Settings.load(),
        'sitemap': PageModel.objects.order_by('headline').values_list(
            'headline',
            'slug'
        )
    }
