from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Post, PostLikes
from django.contrib.auth.models import User

  
class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = ['username']
    
class PostListSerializer(ModelSerializer):
    like_count = serializers.IntegerField()
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'creation_date', 'update_date', 'like_count']    


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']
 
 
class PostlikeSerializer(ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = PostLikes
        fields = ['user', 'creation_date']
