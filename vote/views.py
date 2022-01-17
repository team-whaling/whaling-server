from rest_framework import viewsets

from .serializers import *


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
