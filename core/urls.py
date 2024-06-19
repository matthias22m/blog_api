from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import CategoryViewSet, PostViewSet, CommentViewSet, LikedItemViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'liked_items', LikedItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]