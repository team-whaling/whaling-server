from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response

from account.serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
