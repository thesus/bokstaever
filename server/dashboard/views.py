from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView, FormView
from django.views.generic.base import TemplateView
from django.views.decorators.http import require_POST

from django.http import JsonResponse

from bokstaever.models import (
    Post,
    DatabasePage,
)

import random

from images.models import Image

from dashboard.forms import PostForm, PageForm, ImageForm


class DashboardListView(ListView):
    paginate_by = 6


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


class PageEdit:
    template_name = "dashboard/page_edit.html"
    success_url = "/dashboard/pages"
    form_class = PageForm
    model = DatabasePage


class PageUpdate(PageEdit, UpdateView):
    pass


class PageCreate(PageEdit, CreateView):
    pass


class ImageListSimple(DashboardListView):
    template_name = "dashboard/image_list_simple.html"
    model = Image

    def get(self, request, *args, **kwargs):
        paginator, page, queryset, _ = self.paginate_queryset(
            self.get_queryset(), self.paginate_by
        )
        result = []
        for entry in queryset:
            result.append((entry.id, entry.thumbnail.image_file.url))

        return JsonResponse(
            {
                "result": result,
                "current": page.number,
                "count": paginator.count,
                "pages": paginator.num_pages,
            },
            status=200,
        )


class ImageList(DashboardListView):
    template_name = "dashboard/image_list.html"
    model = Image


class ImageCreate(TemplateView):
    template_name = "dashboard/image_create.html"

@require_POST
def image_upload(request):
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        instance = Image()
        instance.save(
            image=request.FILES["image"], title=form.cleaned_data["title"]
        )

        r = random.randint(0, 10)
        print(r)
        if r > 5:
            return JsonResponse({"detail": instance.pk }, status=200)
    return JsonResponse({"detail": form.errors }, status=400)
