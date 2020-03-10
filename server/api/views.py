from django.db.models.functions import TruncMonth
from django.db.models import Count

from collections import defaultdict

from datetime import datetime

from bokstaever.models import Post, DatabasePage, Gallery

from images.models import Image

from api.serializers import (
    PostSerializer,
    PostListSerializer,
    ImageSerializer,
    ImageCreateSerializer,
    StatisticsSerializer,
    PageSerializer,
    PageListSerializer,
    GallerySerializer,
    GalleryListSerializer,
)

from api.viewsets import MultiSerializerViewSet

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
)

from rest_framework.response import Response


class PostViewSet(MultiSerializerViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_action_classes = {"list": PostListSerializer}
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Exclude posts marked as drafts for anonymous users
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset
        else:
            return self.queryset.filter(draft=False)

    def perform_update(self, serializer):
        serializer.instance.editors.add(self.request.user.pk)
        serializer.instance.save()
        super(PostViewSet, self).perform_update(serializer)

    def perform_create(self, serializer):
        serializer.save(editors=[self.request.user.pk])


class ImageViewSet(MultiSerializerViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    serializer_action_classes = {"create": ImageCreateSerializer}
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Image()
        instance.save(**serializer.validated_data)

        return Response({"id": instance.pk})


class PageViewSet(MultiSerializerViewSet):
    queryset = DatabasePage.objects.all()
    serializer_class = PageSerializer
    serializer_action_classes = {"list": PageListSerializer}
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "slug"


class GalleryViewSet(MultiSerializerViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    serializer_action_classes = {"list": GalleryListSerializer}
    permission_classes = (IsAuthenticatedOrReadOnly,)


class StatisticsView(RetrieveAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        post_count = Post.objects.all().count()
        ppm = (
            Post.objects.filter()
            .annotate(m=TruncMonth("published"))
            .values("m")
            .annotate(c=Count("id"))
            .order_by()
        )

        today = datetime.today()
        data = {}

        activities = defaultdict(dict)
        for a in ppm:
            activities[a["m"].year][a["m"].month] = a["c"]

        for i in range(0, 3):
            year = today.year - i
            data[year] = []
            for month in range(1, 13):
                try:
                    data[year].append((month, activities[year][month]))
                except KeyError:
                    data[year].append((month, 0))
        return {"post_count": post_count, "activity": data}
