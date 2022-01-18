from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from account.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @action(methods=['patch'], detail=False)
    def nickname(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
