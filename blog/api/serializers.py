from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post
from .models import Like


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    Likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner','Likes']


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    Likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','posts','Likes']

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'Likes', 'owner', 'post']

