from rest_framework import viewsets
from.models import Post, Category, LikedItem, Comment
from.serializers import PostSerializer, CategorySerializer, LikedItemSerializer, CommentSerializer
from.permissions import IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # General read/write access control

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthorOrReadOnly]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly]

        return super().get_permissions()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikedItemViewSet(viewsets.ModelViewSet):
    queryset = LikedItem.objects.all()
    serializer_class = LikedItemSerializer
