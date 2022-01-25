from django.contrib.auth import get_user_model
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

    def list_my_page_votes(self, queryset, params):
        # 상태별 투표 개수 계산
        ongoing_votes = queryset.filter(state=Vote.StateOfVote.ONGOING)
        finished_votes = queryset.exclude(state=Vote.StateOfVote.ONGOING)
        count = {
            'ongoing': ongoing_votes.count(),
            'finished': finished_votes.count()
        }

        # 파라미터에 따라 상태별 투표 목록 필터링
        state = params.get('state', None)
        if state == Vote.StateOfVote.ONGOING:
            queryset = ongoing_votes
        elif state == Vote.StateOfVote.FINISHED:
            queryset = finished_votes

        serializer = vote_serializers.MyPageVoteSerializer(queryset, many=True)
        data = {
            'count': count,
            'votes': serializer.data
        }
        return data

    @action(methods=['get'], detail=False, url_path='created-votes')
    def created_votes(self, request):
        queryset = request.user.created_votes.all()
        data = self.list_my_page_votes(queryset, request.query_params)
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='participated-votes')
    def participated_votes(self, request):
        queryset = request.user.participated_votes.all()
        data = self.list_my_page_votes(queryset, request.query_params)
        return Response(data, status=status.HTTP_200_OK)
