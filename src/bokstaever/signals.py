from django.core.cache import caches
from django.dispatch import receiver
from django.db.models.signals import (
    m2m_changed,
    post_delete,
    post_save,
)

from .views import (
    CACHE_NAME,
    MAIN_CACHE_VERSION_KEY,
)


@receiver(m2m_changed)
@receiver(post_delete)
@receiver(post_save)
def bump_global_cache(sender, **kwargs):
    cache = caches[CACHE_NAME]
    current_version = cache.get(MAIN_CACHE_VERSION_KEY)
    if current_version is None:
        cache.set(MAIN_CACHE_VERSION_KEY, 1)
    else:
        cache.incr(MAIN_CACHE_VERSION_KEY)
