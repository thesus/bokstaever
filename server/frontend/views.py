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


class BlogView(DatabaseAwareCacheMixin, ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.filter(draft=False)

    def get_paginate_by(self, queryset):
        return Settings.load().pagesize

    def get_template_names(self):
        theme = Settings.load().theme
        return 'layouts/{0}/blog.html'.format(theme)


class IndexView(DatabaseAwareCacheMixin, TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Specify context on a per template basis
        # context['posts'] = Post.objects.filter(draft=False).order_by('-pk')[:4]

        return context

    def get_template_names(self):
        theme = Settings.load().theme
        return 'layouts/{0}/index.html'.format(theme)


class PostView(DatabaseAwareCacheMixin, DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name_field = 'post'

    def get_template_names(self):
        theme = Settings.load().theme
        return 'layouts/{0}/post.html'.format(theme)


class PageView(DatabaseAwareCacheMixin, DetailView):
    model = Page
    template_name = 'frontend/page.html'
    template_name_field = 'page'

    def get_template_names(self):
        theme = Settings.load().theme
        return 'layouts/{0}/page.html'.format(theme)
