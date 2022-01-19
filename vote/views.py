from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action, api_view

from .serializers import vote_serializers, choice_serializers
from .models import Vote


class VoteViewSet(viewsets.GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = vote_serializers.VoteCreateSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = vote_serializers.VoteListSerializer(
            queryset,
            many=True,
            context={'user': request.user}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        vote = get_object_or_404(queryset, pk=pk)
        serializer = vote_serializers.VoteDetailSerializer(vote, context={'user': request.user})
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
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
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def acc_percent_of_whaling(request):
    total_votes = Vote.objects.all().count()
    correct_votes = Vote.objects.filter(is_answer=True).count()
    acc_percent = correct_votes / total_votes
    data = {
        'acc_percent': acc_percent
    }
    return Response(data)
