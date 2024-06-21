from rest_framework import viewsets
from.models import Post, Category, LikedItem, Comment
from.serializers import PostSerializer, CategorySerializer, LikedItemSerializer, CommentSerializer
from.permissions import IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthorOrReadOnly]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]

        return super().get_permissions()
    
    def create(self, request, *args, **kwargs):
        author_id = request.user.id
        
        serializer = self.get_serializer(data={**request.data, 'author': author_id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author.id!= request.user.id:
            raise PermissionDenied("Only the author can update this post.")
        return super().update(request, *args, **kwargs)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikedItemViewSet(viewsets.ModelViewSet):
    queryset = LikedItem.objects.all()
    serializer_class = LikedItemSerializer
