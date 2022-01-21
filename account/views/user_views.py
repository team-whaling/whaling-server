from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from account.serializers import UserSerializer
from vote.serializers import vote_serializers
from vote.models import Vote

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['patch'], detail=False)
    def nickname(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='created-votes')
    def created_votes(self, request):
        queryset = request.user.created_votes.all()
        ongoing_count = queryset.filter(state=Vote.StateOfVote.ONGOING).count()
        finished_count = queryset.filter(Q(state=Vote.StateOfVote.FINISHED) | Q(state=Vote.StateOfVote.TRACKED)).count()
        serializer = vote_serializers.MyPageVoteSerializer(queryset, many=True)
        data = {
            'ongoing_count': ongoing_count,
            'finished_count': finished_count,
            'votes': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='participated-votes')
    def participated_votes(self, request):
        queryset = request.user.participated_votes.all()
        ongoing_count = queryset.filter(state=Vote.StateOfVote.ONGOING).count()
        finished_count = queryset.filter(Q(state=Vote.StateOfVote.FINISHED) | Q(state=Vote.StateOfVote.TRACKED)).count()
        serializer = vote_serializers.MyPageVoteSerializer(queryset, many=True)
        data = {
            'ongoing_count': ongoing_count,
            'finished_count': finished_count,
            'votes': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
