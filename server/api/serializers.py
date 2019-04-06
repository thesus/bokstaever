from rest_framework import serializers


from bokstaever.models import (
    Post,
    Image,
    Settings,
    Page,
    Gallery
)


class ImageField(serializers.ReadOnlyField):

    def to_representation(self, obj):
        try:
            return obj.url
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
            'slug'
        )


class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(use_url=True, read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'title', 'image', 'thumbnail')


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Settings
        fields = (
            'name',
            'email',
            'info',
            'description',
            'image',
            'theme',
            'pagesize'
        )


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
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
        model = Page
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
