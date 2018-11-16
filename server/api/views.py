from django.db.models.functions import TruncMonth
from django.db.models import Count

from collections import defaultdict

from datetime import datetime

from bokstaever.models import (
    Post,
    Image,
    Page,
    Gallery,

    Settings
)

from api.serializers import (
    PostSerializer,
    PostListSerializer,

    ImageSerializer,

    SettingsSerializer,
    StatisticsSerializer,

    PageSerializer,
    PageListSerializer,

    GallerySerializer,
    GalleryListSerializer
)

from api.viewsets import (MultiSerializerViewSet)

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from rest_framework.generics import (
    RetrieveAPIView,
    UpdateAPIView,
)

from rest_framework.viewsets import (
    ModelViewSet
)


class PostViewSet(MultiSerializerViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_action_classes = {
        'list': PostListSerializer
    }
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.instance.editors.add(self.request.user.pk)
        serializer.instance.save()
        super(PostViewSet, self).perform_update(serializer)

    def perform_create(self, serializer):
        serializer.save(
            editors=[self.request.user.pk]
        )


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)


class SettingsUpdateView(RetrieveAPIView,
                         UpdateAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self):
        return Settings.load()


class PageViewSet(MultiSerializerViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    serializer_action_classes = {
        'list': PageListSerializer
    }
    permussion_class = (IsAuthenticated, )
    lookup_field = 'slug'


class GalleryViewSet(MultiSerializerViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    serializer_action_classes = {
        'list': GalleryListSerializer
    }
    permission_class = (IsAuthenticated, )


class StatisticsView(RetrieveAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        post_count = Post.objects.all().count()
        ppm = Post.objects.filter(
        ).annotate(
            m=TruncMonth('published')
        ).values('m').annotate(c=Count('id')).order_by()

        today = datetime.today()
        data = {}

        activities = defaultdict(dict)
        for a in ppm:
            activities[a['m'].year][a['m'].month] = a['c']

        for i in range(0, 3):
            year = today.year - i
            data[year] = []
            for month in range(1, 13):
                try:
                    data[year].append(
                        (
                            month,
                            activities[year][month]
                        )
                    )
                except KeyError:
                    data[year].append((month, 0))
        return {
            'post_count': post_count,
            'activity': data
        }
