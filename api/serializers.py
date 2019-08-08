from rest_framework import serializers
from .models import Post,People


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'imgName',
            'title',
            'link',
            'created_at',
        )
        read_only_fields = ('created_at',)

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = (
            'imgName',
            'name',
            'subname',
            'title',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
