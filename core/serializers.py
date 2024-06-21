from rest_framework import serializers
from .models import Category, Comment, Post, LikedItem
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)
    category = serializers.SlugRelatedField(
        slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_on', 'category']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'author': {
                'read_only': True
            },
            'created_on': {
                'read_only': True
            },
        }
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = UserSerializer(
            instance.author, many=False).data
        return representation



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_on', 'author', 'post']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'author': {
                'read_only': True
            },
            'created_on': {
                'read_only': True
            },
        }


class LikedItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=False)
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), many=False)

    class Meta:
        model = LikedItem
        fields = ['id', 'created_at', 'updated_at', 'user', 'post']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'updated_at': {
                'read_only': True
            },
            'created_at': {
                'read_only': True
            },
        }
