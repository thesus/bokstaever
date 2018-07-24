from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from bokstaever.models import Post


class PostListView(ListView):
    model = Post

    template_name = 'bokstaever/index.html'
    paginate_by = 4


class PostDetailView(DetailView):
    model = Post
    template_name = 'bokstaever/detail.html'
