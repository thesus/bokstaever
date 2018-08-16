from django.core.cache import caches


class DatabaseAwareCacheMixin:
    """
    This is a simple cache mixin for web applications that use very little
    database write operations.

    Use this mixin in your class-based views. They will all share one global
    version, that is incremented, if anything is updated in the database.
    Every piece of cached data also has a verson attached to it. If this
    version is less than the global version, the view-logic is rendered again.
    """

    cache_name = 'default'
    main_cache_version_key = 'version'

    def dispatch(self, request, *args, **kwargs):
        if request.method not in ('HEAD', 'GET'):
            # Don't bother checking cache.
            return super().dispatch(request, *args, **kwargs)

        url = request.build_absolute_uri()
        url_version_key = 'ver\0' + url
        url_version = self.cache.get(url_version_key, -1)
        if url_version is not None:
            try:
                url_version = int(url_version)
            except ValueError:
                self.cache.delete(url_version_key)
                url_version = -1
        version = self.cache.get(self.main_cache_version_key, 0)
        url_cache_key = 'data\0' + url
        response = None
        if version <= url_version:
            response = self.cache.get(url_cache_key)
        if response is None:
            # There is nothing in the cache or it is too old.
            response = super().dispatch(request, *args, **kwargs)
            self.cache.set(url_cache_key, response)
            self.cache.set(url_version_key, version)
            return response
        else:
            return response

    @property
    def cache(self):
        return caches[self.cache_name]
