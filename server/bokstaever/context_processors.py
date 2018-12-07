from bokstaever.models import (
    Settings,
    Page
)


def info(request):
    return {
        'settings': Settings.load(),
        'sitemap': Page.objects.order_by('headline').values_list(
            'headline',
            'slug'
        )
    }
