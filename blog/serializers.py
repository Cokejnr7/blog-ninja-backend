from rest_framework import serializers
from users.models import CustomUser
from .models import Post
from users.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'id', 'author']
