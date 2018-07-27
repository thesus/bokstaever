from rest_framework import serializers

from bokstaever.models import (
    Post,
    Image,
    Settings
)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'headline',
            'image',
            'text',
            'published',
            'draft',
            'editors'
        )
        read_only_fields = ('editors', )


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
            'editors'
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
