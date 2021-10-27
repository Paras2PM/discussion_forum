from rest_framework.response import Response
from api.models import Post, PostLikes
from api.serializers import PostListSerializer, PostCreateUpdateSerializer, PostlikeSerializer
from rest_framework import permissions, status, viewsets
from .permissions import IsAuthorOrReadOnly
from django.db.models import Count

    
# GET, POST, PUT, and DELETE method handlers for Posts:
class PostUpdaAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Post.objects.annotate(like_count=Count('post_like')).order_by('-creation_date')
        return Post.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
   
    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostListSerializer
        if self.action in ['create', 'update']:
            return PostCreateUpdateSerializer
        if self.action == 'destroy':
            return PostListSerializer
       
       
# GET, POST, and DELETE method handlers for Posts' likes:
class PostLikeAPIView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def list(self, request, pk):
        queryset  = PostLikes.objects.filter(post__id=pk)
        serializer = PostlikeSerializer(queryset , many=True)
        return Response(serializer.data)
        
    def create(self, request, pk):
        liked_by_user = PostLikes.objects.filter(post__id=pk, user=request.user).exists()
        if liked_by_user:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'This post already liked by you'
            })
        PostLikes.objects.create(user=request.user, post_id=pk)
        return Response({
                'status': status.HTTP_200_OK,
            })
         
    def destroy(self, request, pk):
        result = PostLikes.objects.filter(post__id=pk, user=request.user).delete()
        if result[0] == 0:
            return Response({"message": "Error!", 'status': status.HTTP_404_NOT_FOUND})
        return Response({
                'status': status.HTTP_200_OK,
            })
            