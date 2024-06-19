from rest_framework import status, viewsets
from rest_framework.response import Response
from.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(pk=user.pk)
