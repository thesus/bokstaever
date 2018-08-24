from django.core.cache import caches


MAIN_CACHE_VERSION_KEY = 'version'
CACHE_NAME = 'default'


class DatabaseAwareCacheMixin:
    """
    This is a simple cache mixin for web applications that use very little
    database write operations.

    Use this mixin in your class-based views. They will all share one global
    version, that is incremented, if anything is updated in the database.
    Every piece of cached data also has a verson attached to it. If this
    version is less than the global version, the view-logic is rendered again.
    """

    def dispatch(self, request, *args, **kwargs):
        if request.method not in ('HEAD', 'GET'):
            # Don't bother checking cache.
            return super().dispatch(request, *args, **kwargs)

        url = request.build_absolute_uri()
        url_version_key = 'ver/0' + url
        url_version = self.cache.get(url_version_key, -1)
        if url_version is not None:
            try:
                url_version = int(url_version)
            except ValueError:
                self.cache.delete(url_version_key)
                url_version = -1
        version = self.cache.get(MAIN_CACHE_VERSION_KEY, 0)
        url_cache_key = 'data/0' + url
        response = None
        if version <= url_version:
            response = self.cache.get(url_cache_key)
        if response is None:
            # There is nothing in the cache or it is too old.
            response = super().dispatch(request, *args, **kwargs)
            self.cache.set(url_cache_key, response.render())
            self.cache.set(url_version_key, version)
            return response
        else:
            return response

    @property
    def cache(self):
        return caches[CACHE_NAME]
