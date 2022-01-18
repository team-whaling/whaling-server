from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import coin_serializers, vote_serializers, choice_serializers
from .models import Vote, Choice, Coin


class VoteViewSet(viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = vote_serializers.VoteListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        for data in serializer.data:
            participants = data.pop('participants')
            if request.user.user_id in participants:
                voted = True
            else:
                voted = False
            data['user'] = {
                'voted': voted
            }
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        vote = get_object_or_404(queryset, pk=pk)
        serializer = vote_serializers.VoteDetailSerializer(vote)
        data = serializer.data
        try:
            choice_obj = Choice.objects.get(vote_id=pk, participant_id=request.user.user_id)
            choice = choice_obj.choice
            is_answer = choice_obj.is_answer
        except Choice.DoesNotExist:
            choice = is_answer = None
        data['user'] = {
            'choice': choice,
            'is_answer': is_answer
        }
        return Response(data)

    def create(self, request):
        serializer = vote_serializers.VoteCreateSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        vote = serializer.save()
        data = {
            'vote_id': vote.vote_id
        }
        return Response(data)

    @action(detail=True, methods=['post'])
    def choice(self, request, pk=None):
        request.data['vote'] = pk
        serializer = choice_serializers.ChoiceSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        choice_obj = serializer.save()
        data = {
            'vote_id': choice_obj.vote_id,
            'choice': choice_obj.choice
        }
        return Response(data)


# class VoteModelViewSet(viewsets.ModelViewSet):
#     serializer_class = VoteCreateSerializer
#     queryset = Vote.objects.all()


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = choice_serializers.ChoiceSerializer
    queryset = Choice.objects.all()
