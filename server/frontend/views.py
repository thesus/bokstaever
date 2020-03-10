from django.http import Http404

from django.views.generic import DetailView, ListView

from bokstaever.models import Post, FilePage, DatabasePage, Settings

from bokstaever.views import DatabaseAwareCacheMixin


class BundleMixin:
    def get_template_names(self) -> str:
        try:
            return "default/{0}".format(self.template)
        except NameError:
            raise Exception("You have to define a template name.")


class IndexView(DatabaseAwareCacheMixin, BundleMixin, ListView):
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(draft=False)
    template = "index.html"

    def get_paginate_by(self, queryset) -> int:
        return Settings.load().pagesize


class PostView(DatabaseAwareCacheMixin, BundleMixin, DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name_field = "post"
    template = "post.html"


class PageView(DatabaseAwareCacheMixin, BundleMixin, DetailView):
    template = "page.html"
    context_object_name = "page"

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        obj = None
        try:
            obj = DatabasePage.objects.filter(slug=slug).get()
        except DatabasePage.DoesNotExist:
            try:
                obj = FilePage.objects.filter(slug=slug).get()
            except FilePage.DoesNotExist:
                raise Http404("The page you're looking for does not exist.")

        return obj

    def get_template_names(self):
        if isinstance(self.object, FilePage):
            return self.object.path
        else:
            return super().get_template_names()
