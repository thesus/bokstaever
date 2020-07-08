from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _
from django.core import serializers
from django.http import JsonResponse

from bokstaever.models import Post
from images.models import Image

from django import forms

from dashboard.fields import ImageChoiceField

class DashboardListView(ListView):
    paginate_by = 6

class ImageListSimple(DashboardListView):
    template_name = "dashboard/image_list_simple.html"
    model = Image

    def get(self, request, *args, **kwargs):
        paginator, page, queryset, _ = self.paginate_queryset(self.get_queryset(), self.paginate_by)
        result = []
        for entry in queryset:
            result.append((entry.id, entry.thumbnail.image_file.url))

        return JsonResponse({'result': result, 'current': page.number, 'count': paginator.count, 'pages': paginator.num_pages }, status=200)


class PostList(DashboardListView):
    model = Post
    template_name = "dashboard/post_list.html"


class PostForm(forms.ModelForm):
    image = ImageChoiceField()

    class Meta:
        model = Post
        fields = ['headline', 'draft', 'text', 'type', 'image']

class PostEdit():
    template_name = "dashboard/post_edit.html"
    success_url = "/dashboard/posts"
    form_class = PostForm
    model = Post

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        return form

class PostUpdate(PostEdit, UpdateView):
    pass

class PostCreate(PostEdit, CreateView):
    pass
