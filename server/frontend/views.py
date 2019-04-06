from django.shortcuts import redirect

from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)

from bokstaever.models import (
    Post,
    Page,
    Settings
)

from bokstaever.views import DatabaseAwareCacheMixin

class BundleMixin():
    def get_template_names(self) -> str:
        bundle = Settings.load().bundle
        try:
            return 'bundles/{0}/{1}'.format(bundle.slug, self.template)
        except NameError:
            raise Exception("You have to define a template name.")


class BlogView(DatabaseAwareCacheMixin, BundleMixin, ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(draft=False)
    template = 'blog.html'

    def get_paginate_by(self, queryset) -> int:
        return Settings.load().pagesize


class IndexView(DatabaseAwareCacheMixin, BundleMixin, TemplateView):
    template = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Specify context on a per template basis
        # context['posts'] = Post.objects.filter(draft=False).order_by('-pk')[:4]

        return context


class PostView(DatabaseAwareCacheMixin, BundleMixin, DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name_field = 'post'
    template = 'post.html'


class PageView(DatabaseAwareCacheMixin, BundleMixin, DetailView):
    model = Page
    template = 'page.html'
    template_name_field = 'page'
