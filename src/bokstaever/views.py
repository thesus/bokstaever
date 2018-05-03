from django.views.generic.list import ListView

from bokstaever.models import Post

class PostListView(ListView):
    model = Post

    template_name = 'bokstaever/index.html'
    paginate_by = 9
