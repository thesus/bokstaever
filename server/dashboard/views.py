from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.views.generic.base import TemplateView

from django.http import JsonResponse

from bokstaever.models import Post, DatabasePage, FilePage

from images.models import Image

from dashboard.forms import PostForm, PageForm


class DashboardListView(ListView):
    paginate_by = 16


class PostList(DashboardListView):
    model = Post
    template_name = "dashboard/post_list.html"


class PostEdit:
    template_name = "dashboard/post_edit.html"
    success_url = "/dashboard/posts"
    form_class = PostForm
    model = Post


class PostUpdate(PostEdit, UpdateView):
    pass


class PostCreate(PostEdit, CreateView):
    pass


class PageList(DashboardListView):
    template_name = "dashboard/page_list.html"
    model = DatabasePage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Insert all filepages
        # Since we don't expect that many there's no pagination
        context["file_pages"] = FilePage.objects.all()

        return context


class PageEdit:
    template_name = "dashboard/page_edit.html"
    success_url = "/dashboard/pages"
    form_class = PageForm
    model = DatabasePage


class PageUpdate(PageEdit, UpdateView):
    pass


class PageCreate(PageEdit, CreateView):
    pass


class ImageList(DashboardListView):
    template_name = "dashboard/image_list.html"
    ordering = ["-creation_date"]
    model = Image


class ImageCreate(TemplateView):
    template_name = "dashboard/image_create.html"
