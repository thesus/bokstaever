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


class IndexSiteView(DatabaseAwareCacheMixin, TemplateView):
    template_name = 'frontend/site/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(draft=False).order_by('-pk')[:4]

        return context


class BlogView(DatabaseAwareCacheMixin, ListView):
    model = Post
    template_name = 'frontend/site/blog.html'
    context_object_name = 'posts'
    # paginate_by = 4
    queryset = Post.objects.filter(draft=False)

    def get_paginate_by(self, queryset):
        return Settings.load().pagesize


class IndexBlogView(BlogView):
    template_name = 'frontend/blog/index.html'


def index(request):
    settings = Settings.load()
    behaviors = {
        'site': IndexSiteView.as_view(),
        'blog': IndexBlogView.as_view()
    }
    return behaviors[settings.behavior](request)


def blog(request):
    settings = Settings.load()
    if settings.behavior == 'site':
        return BlogView.as_view()(request)
    else:
        return redirect('index')


class PostView(DatabaseAwareCacheMixin, DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name = 'frontend/post.html'
    template_name_field = 'post'


class PageView(DatabaseAwareCacheMixin, DetailView):
    model = Page
    template_name = 'frontend/page.html'
    template_name_field = 'page'
