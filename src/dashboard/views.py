from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

from dashboard.forms import ImageForm
from dashboard.images import save_image

from threading import Thread

class ImageView(View):
    form_class = ImageForm
    template_name = 'dashboard/image/upload.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            save_image(form.cleaned_data['image'], 'aaa')
            return JsonResponse({'message': 'Successful'})

        return JsonResponse({'message': form.errors})
