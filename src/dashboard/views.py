from django.urls import reverse_lazy

from django.views.generic import (
    TemplateView,
    ListView
)

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    FormView
)

from bokstaever.models import (
    Post,
    Image,
    Settings
)

from dashboard.api import (
    AjaxResponseMixin,
    AjaxSerializeMixin,
    AjaxSerializeListMixin
)

from dashboard.forms import (
    ImageForm,
)


class DashboardIndex(AjaxSerializeMixin,
                     ListView):
    model = Post
    template_name = 'dashboard/index.html'


class ImageViewMixin:
    form_class = ImageForm
    template_name = 'dashboard/image/upload.html'
    success_url = reverse_lazy('dashboard:image-create')

    def form_valid(self, form):
        form.create_images()
        return super().form_valid(form)


class ImageCreate(ImageViewMixin,
                  AjaxResponseMixin,
                  FormView):
    pass

class SettingsViewMixin:
    fields = ['name', 'email', 'info']
    template_name = 'dashboard/settings.html'

    def get_object(self):
        return Settings.load()


class SettingsUpdate(SettingsViewMixin,
                     AjaxResponseMixin,
                     UpdateView):
    pass


class PostViewMixin:
    model = Post
    fields = ['headline', 'text', 'image']
    template_name = 'dashboard/post/edit.html'

    def form_valid(self, form):
        self.object = form.save()
        self.object.editors.add(self.request.user)
        self.object.save()
        return super().form_valid(form)


class PostCreate(PostViewMixin,
                 AjaxResponseMixin,
                 CreateView):
    pass


class PostUpdate(PostViewMixin,
                 AjaxResponseMixin,
                 UpdateView):
    pass


class PostList(
        AjaxSerializeListMixin,
        ListView):
    model = Post
    template_name = 'dashboard/post/list.html'
    paginate_by = 2
    fields = ['pk', 'headline', 'published', 'draft']

class ImageList(
        AjaxSerializeListMixin,
        ListView):
    model = Image
    paginate_by = 18
    template_name = 'dashboard/image/list.html'
    fields = ['pk', 'title', 'path']
