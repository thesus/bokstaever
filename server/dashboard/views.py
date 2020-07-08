from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from django.core import serializers
from django.http import JsonResponse

from bokstaever.models import (
    Post,
    DatabasePage,
    FilePage,
    PageModel
)
from images.models import Image

from django import forms

from dashboard.fields import ImageChoiceField


class DashboardListView(ListView):
    paginate_by = 6


class PostList(DashboardListView):
    model = Post
    template_name = "dashboard/post_list.html"


class PostForm(forms.ModelForm):
    image = ImageChoiceField()

    class Meta:
        model = Post
        fields = ["headline", "draft", "text", "type", "image"]


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


class PageForm(forms.ModelForm):
    image = ImageChoiceField()

    class Meta:
        model = DatabasePage
        fields = ["headline", "show_menu", "text", "type", "draft", "image"]


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

class ImageCreate()
