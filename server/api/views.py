from django.views.generic import ListView
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from images.models import Image

from api.forms import ImageForm

class ImageList(ListView):
    paginate_by = 9
    model = Image

    def get(self, request, *args, **kwargs):
        paginator, page, queryset, _ = self.paginate_queryset(
            self.get_queryset(), self.paginate_by
        )
        result = []
        for entry in queryset:
            result.append(
                (entry.id, entry.thumbnail.image_file.url if entry.thumbnail else "")
            )

        return JsonResponse(
            {
                "result": result,
                "current": page.number,
                "count": paginator.count,
                "pages": paginator.num_pages,
            },
            status=200,
        )

@require_POST
def image_upload(request):
    form = ImageForm(request.POST, request.FILES)

    if form.is_valid():
        instance = Image()
        instance.save(
            image=request.FILES["image"], title=form.cleaned_data["title"]
        )

        return JsonResponse({"detail": instance.pk }, status=200)
    return JsonResponse({"detail": form.errors }, status=400)
