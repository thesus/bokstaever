from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

from dashboard.forms import ImageForm

class ImageView(View):
    form_class = ImageForm
    template_name = 'dashboard/image/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return JsonResponse({'message': 'Successful'})

        return render(request, self.template_name, {'form': form})
