from django.views.generic import ListView, View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from images.models import Image

from api.forms import ImageForm


class ImageList(ListView):
    """Returns a json response containing a paginated image list.

    - GET parameter `detailed` returns all urls, instead of only the thumbnail url.
    - GET parameter `all` returns all images and not only images marked for the feed,
      given the feed is enabled, only works for authenticated users.

    Output format:
    ```json
    {
        result: [],  // List of images
        current: 1,  // Page number
        count: 20,   // Amount of images
        pages: 3,    // Amount of pages
    }
    ```
    """

    paginate_by = 12
    queryset = Image.objects.filter(thumbnail__isnull=False)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by("-creation_date")

        # Only return all images if requested and the user is authenticated
        # Otherwise only return images marked for the feed if the feed is enabled
        if "all" in self.request.GET.keys() and self.request.user.is_authenticated:
            queryset = queryset
        else:
            # Unauthenticated users can only get images marked for the feed.
            if settings.INCLUDE_IMAGE_FEED:
                queryset = queryset.filter(feed=True)
            else:
                return JsonResponse({"detail": "Not allowed."}, status=403)

        paginator, page, queryset, _ = self.paginate_queryset(
            queryset, self.paginate_by
        )

        # If a `detailed` parameter is given, return all dimensions instead of only the thumbnail
        result = []
        if "detailed" in self.request.GET.keys():
            for entry in queryset:
                result.append(
                    (
                        entry.id,
                        entry.thumbnail.image_file.url,
                        entry.get_files(),
                        entry.title,
                        entry.creation_date,
                    )
                )
        else:
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
