from rest_framework import serializers
from .models import Post, PostHistory


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user_id', 'post_id', 'likes',)


class PostHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHistory
        fields = ('user_id', 'post_id', 'likes', 'created_at')