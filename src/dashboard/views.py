from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Value, CharField, Count
from django.db.models.functions import TruncMonth

from collections import defaultdict

from datetime import datetime

from django.http import JsonResponse

from django_rq import get_queue

from bokstaever.models import Post, DatabasePage, FilePage, Gallery

from images.models import Image

from dashboard.forms import PostForm, PageForm, ImageForm, GalleryForm


class DeleteView(LoginRequiredMixin, DeleteView):
    def get(self, request, pk, **kwargs):
        return JsonResponse({"pk": pk}, status=200)


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def count_posts():
        def scale(value):
            if value == 1:
                return 0.4
            elif value < 3:
                return 0.7
            else:
                return 1

        post_count = Post.objects.all().count()

        ppm = (
            Post.objects.filter()
            .annotate(m=TruncMonth("published"))
            .values("m")
            .annotate(c=Count("id"))
            .order_by()
        )

        today = datetime.today()
        data = {}

        activities = defaultdict(dict)
        for a in ppm:
            activities[a["m"].year][a["m"].month] = scale(a["c"])

        for i in range(0, 3):
            year = today.year - i
            data[year] = []
            for month in range(1, 13):
                try:
                    data[year].append((month, activities[year][month]))
                except KeyError:
                    data[year].append((month, 0.1))

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["statistics"] = {}
        context["statistics"]["activity"] = Dashboard.count_posts()
        return context


class DashboardListView(LoginRequiredMixin, ListView):
    paginate_by = 16


class PostList(DashboardListView):
    model = Post
    template_name = "dashboard/post_list.html"


class PostEdit(LoginRequiredMixin):
    template_name = "dashboard/post_edit.html"
    success_url = "/dashboard/posts"
    form_class = PostForm
    model = Post


class PostUpdate(PostEdit, UpdateView):
    pass


class PostCreate(PostEdit, CreateView):
    pass


class PostDelete(PostEdit, DeleteView):
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


class PageEdit(LoginRequiredMixin):
    template_name = "dashboard/page_edit.html"
    success_url = "/dashboard/pages"
    form_class = PageForm
    model = DatabasePage


class PageUpdate(PageEdit, UpdateView):
    pass


class PageCreate(PageEdit, CreateView):
    pass


class PageDelete(PageEdit, DeleteView):
    pass


class ImageList(DashboardListView):
    paginate_by = 36

    template_name = "dashboard/image_list.html"
    ordering = ["-creation_date"]
    queryset = Image.objects.filter(thumbnail__isnull=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        queue = get_queue("default")
        count = len(queue.jobs) + queue.started_job_registry.count

        context["processing_count"] = count
        context["is_processing"] = count > 0

        return context


class ImageUpdate(LoginRequiredMixin, UpdateView):
    template_name = "dashboard/image_edit.html"
    success_url = "/dashboard/images"
    model = Image
    form_class = ImageForm


class ImageCreate(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/image_create.html"


class ImageDelete(DeleteView):
    success_url = "/dashboard/images"
    model = Image


class GalleryList(DashboardListView):
    template_name = "dashboard/gallery_list.html"
    ordering = ["-id"]
    model = Gallery


class GalleryEdit(LoginRequiredMixin):
    template_name = "dashboard/gallery_edit.html"
    success_url = "/dashboard/galleries"
    form_class = GalleryForm
    model = Gallery


class GalleryCreate(GalleryEdit, CreateView):
    pass


class GalleryDelete(GalleryEdit, DeleteView):
    pass


class GalleryUpdate(GalleryEdit, UpdateView):
    pass
