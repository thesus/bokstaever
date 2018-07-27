from rest_framework import serializers

from bokstaever.models import (
    Post,
    Image,
    Settings
)

class PostSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image_title = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'text',
            'published',
            'draft',
            'editors',
            'image',
            'image_url',
            'image_title'
        )
        read_only_fields = ('editors', )

    def get_image_url(self, instance):
        return instance.image.image.url

    def get_image_title(self, instance):
        return instance.image.title


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
    class Meta:
        model = Image
        fields = ('id', 'title', 'image')


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title')


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ('name', 'email', 'info')
