from rest_framework import serializers


from bokstaever.models import (
    Post,
    Settings,
    DatabasePage,
    PageModel,
    Gallery
)

from images.models import (
    Image
)


class ImageListingField(serializers.RelatedField):
    def to_representation(self, obj):
        try:
            return obj.image_file.url
        except AttributeError:
            return ''

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'text',
            'type',
            'draft',
            'image',
            'editors',
            'published',
        )
        read_only_fields = ('editors', 'published')


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'published',
        )


class ImageSerializer(serializers.ModelSerializer):
    files = ImageListingField(many=True, read_only=True)
    thumbnail = ImageListingField(read_only=True)

    class Meta:
        model = Image
        fields = (
            'id',
            'title',
            'files',
            'thumbnail'
        )


class ImageCreateSerializer(serializers.Serializer):
    image = serializers.ImageField()
    title = serializers.CharField(max_length=200)


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = (
            'name',
            'email',
            'info',
            'pagesize'
        )


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatabasePage
        fields = (
            'headline',
            'slug',
            'text',
            'type',
            'image'
        )
        lookup_field = 'slug'
        read_only_fields = ('slug', )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class PageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageModel
        fields = ('headline', 'slug')


class GalleryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('id', 'name')


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('id', 'name', 'images')


class StatisticsSerializer(serializers.Serializer):
    post_count = serializers.IntegerField()
    activity = serializers.DictField()
