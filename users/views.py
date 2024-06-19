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


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

