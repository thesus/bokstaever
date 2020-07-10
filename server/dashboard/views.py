from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.views.generic.base import TemplateView
from django.db.models import Value, CharField

from django.http import JsonResponse

from bokstaever.models import Post, DatabasePage, FilePage, Gallery

from images.models import Image

from dashboard.forms import PostForm, PageForm, GalleryForm


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

    def get_queryset(self):
        values = ["pk", "headline", "show_menu", "slug", "t"]

        db_page = (
            DatabasePage.objects.all()
            .annotate(t=Value("db", CharField()))
            .values(*values)
        )

        file_page = (
            FilePage.objects.all()
            .annotate(t=Value("file", CharField()))
            .values(*values)
        )

        data = db_page.union(file_page).order_by("t")
        return data


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
    paginate_by = 36

    template_name = "dashboard/image_list.html"
    ordering = ["-creation_date"]
    model = Image


class ImageCreate(TemplateView):
    template_name = "dashboard/image_create.html"


class GalleryList(DashboardListView):
    template_name = "dashboard/gallery_list.html"
    ordering = ["-id"]
    model = Gallery


class GalleryEdit:
    template_name = "dashboard/gallery_edit.html"
    success_url = "/dashboard/galleries"
    form_class = GalleryForm
    model = Gallery

class GalleryCreate(GalleryEdit, CreateView):
    pass

class GalleryUpdate(GalleryEdit, UpdateView):
    pass
