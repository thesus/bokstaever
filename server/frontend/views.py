from django.views.generic import TemplateView

from bokstaever.models import Post

class IndexView(TemplateView):
    template_name = 'frontend/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = Post.objects.filter().order_by('-pk')[:4]
        return context
