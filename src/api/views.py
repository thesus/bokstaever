from django.views.generic import ListView, View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from images.models import Image

from api.forms import ImageForm


class ImageList(ListView):
    """Returns a json response containing a paginated image list."""

    paginate_by = 12
    order_by = ["-creation_date"]
    queryset = Image.objects.filter(thumbnail__isnull=False)

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


class ImageCreate(LoginRequiredMixin, View):
    """Allows uploading of images via a POST request. Returns a json response."""

    def post(self, request):
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            instance = Image()
            instance.save(
                image=request.FILES["image"], title=form.cleaned_data["title"]
            )

            return JsonResponse({"detail": instance.pk}, status=200)
        return JsonResponse({"detail": form.errors}, status=400)
