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

    PageSerializer,
    PageListSerializer,

    GallerySerializer,
    GalleryListSerializer
)

from api.viewsets import (
    MultiSerializerViewSet,
    ConditionalAuthenticationMixin
)

from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

from rest_framework.viewsets import (
    ModelViewSet
)

class PostViewSet(ConditionalAuthenticationMixin,
                  MultiSerializerViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_action_classes = {
        'list': PostListSerializer
    }
    unauthenticated_actions = [
        'list', 'retrieve'
    ]

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

class PageViewSet(ConditionalAuthenticationMixin,
                  MultiSerializerViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    serializer_action_classes = {
        'list': PageListSerializer
    }
    unauthenticated_actions = [
        'list', 'retrieve'
    ]
    lookup_field = 'slug'


class GalleryViewSet(MultiSerializerViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    serializer_action_classes = {
        'list': GalleryListSerializer
    }
    permission_class = (IsAuthenticated,)
