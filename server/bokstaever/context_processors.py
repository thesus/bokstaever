from bokstaever.models import (
    Settings,
    Page
)

def info(request):
    return {
        'settings': Settings.load(),
        'sitemap': Page.objects.values_list('headline', 'slug')
    }
