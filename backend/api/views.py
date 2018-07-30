from bokstaever.models import (
    Post,
    Image,

    Settings
)

from api.serializers import (
    PostSerializer,
    PostListSerializer,

    ImageSerializer,
    ImageListSerializer,

    SettingsSerializer
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

class ImageViewSet(MultiSerializerViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    serializer_action_classes = {
        'list': ImageListSerializer
    }
    permission_classes = (IsAuthenticated,)


class SettingsUpdateView(RetrieveAPIView,
                         UpdateAPIView):
    serializer_class = SettingsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_object(self):
        return Settings.load()
