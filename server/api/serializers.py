from rest_framework import serializers

from bokstaever.models import (
    Post,
    Image,
    Settings,
    Page
)

class ImageField(serializers.ReadOnlyField):

    def to_representation(self, obj):
        try:
            return obj.url
        except AttributeError:
            return ''

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image_title = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'text',
            'published',
            'type',
            'draft',
            'editors',
            'image',
            'image_url',
            'image_title',
            'thumbnail_url'
        )
        read_only_fields = ('editors', )

    def get_image_url(self, instance):
        return instance.image.image.url

    def get_image_title(self, instance):
        return instance.image.title

    def get_thumbnail_url(self, instance):
        return instance.image.thumbnail.url


class PostListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'image',
            'text',
            'published',
            'draft',
            'slug'
        )

    def get_image_url(self, instance):
        return instance.image.image.url

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
            'image',
            'theme',
            'behavior'
        )


class PageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Page
        fields = (
            'headline',
            'slug',
            'text',
            'type',
            'image',
            'image_url'
        )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def get_image_url(self, instance):
        try:
            return instance.image.image.url
        except AttributeError:
            return None


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('headline', 'slug')
