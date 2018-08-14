from django.views.generic import (
    TemplateView,
    DetailView
)

from bokstaever.models import (
    Post,
    Page
)

class IndexView(TemplateView):
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter(draft=False).order_by('-pk')[:4]
        return context

class PostView(DetailView):
    queryset = Post.objects.filter(draft=False)
    template_name = 'frontend/post.html'
    template_name_field = 'post'


class PageView(DetailView):
    model = Page
    template_name = 'frontend/page.html'
    template_name_field = 'page'
