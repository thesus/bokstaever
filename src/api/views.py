from bokstaever.models import (
    Post,
    Image
)

from api.serializers import (
    PostSerializer,
    PostListSerializer,

    ImageSerializer,
    ImageListSerializer
)

from api.viewsets import (
    MultiSerializerViewSet
)

from rest_framework import (
    mixins,
    generics
)

class PostViewSet(MultiSerializerViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_action_classes = {
        'list': PostListSerializer
    }

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
