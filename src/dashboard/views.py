from django.views import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render

from django.core import serializers

from dashboard.forms import (
    ImageForm,
    PostForm
)

from dashboard.images import save_image

from bokstaever.models import Post

class ImageView(View):
    form_class = ImageForm
    template_name = 'dashboard/image/upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            # RQ-worker :)
            save_image(form.cleaned_data['image'], 'aaaeiuae')
            return JsonResponse({'message': 'Successful'})

        return JsonResponse({'message': form.errors})


class PostView(View):
    form_class = PostForm
    template_name = 'dashboard/post/edit.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            if 'id' in kwargs:
                post = Post.objects.filter(pk=kwargs['id'])
                data = serializers.serialize(
                    'json',
                    post,
                    fields=('headline', 'text')
                )
                return HttpResponse(data, content_type='application/json')
            else:
                return JsonResponse({})
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(request.readlines())
        instance = Post.objects.get(pk=kwargs['id'])
        form = self.form_class(request.POST, instance=instance)
        print(form.errors)
        form.save()
        return JsonResponse({})
