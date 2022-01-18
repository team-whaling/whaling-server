from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import coin_serializers, vote_serializers, choice_serializers
from .models import Vote, Choice


class VoteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Vote.objects.all()
    serializer_class = vote_serializers.VoteCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = vote_serializers.VoteListSerializer(queryset, many=True)
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
        serializer = vote_serializers.VoteDetailSerializer(vote, context={'user': request.user})
        return Response(serializer.data)


# class VoteModelViewSet(viewsets.ModelViewSet):
#     serializer_class = VoteCreateSerializer
#     queryset = Vote.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = choice_serializers.ChoiceSerializer
    queryset = Choice.objects.all()
