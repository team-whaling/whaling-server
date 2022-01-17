from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import VoteCreateSerializer, VoteListSerializer, VoteDetailSerializer, ChoiceSerializer
from .models import Vote, Choice


class VoteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Vote.objects.all()
    serializer_class = VoteCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = VoteListSerializer(queryset, many=True)
        for data in serializer.data:
            participants = data.pop('participants')
            if request.user.user_id in participants:
                voted = True
            else:
                voted = False
            data['voted'] = voted
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        vote = get_object_or_404(queryset, pk=pk)
        serializer = VoteDetailSerializer(vote, context={'request': request})
        return Response(serializer.data)


# class VoteModelViewSet(viewsets.ModelViewSet):
#     serializer_class = VoteCreateSerializer
#     queryset = Vote.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
