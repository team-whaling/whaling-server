from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from account.serializers import UserSerializer
from vote.serializers import VoteSerializer
from vote.models import Vote

User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='nickname/check')
    def nickname_check(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({"nickname": "이미 존재하는 닉네임입니다."}, status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['patch'], detail=False)
    def nickname(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def list_my_page_votes(self, queryset, request):
        params = request.query_params
        ongoing_votes = queryset.filter(state=Vote.StateOfVote.ONGOING)
        finished_votes = queryset.exclude(state=Vote.StateOfVote.ONGOING)

        # 파라미터에 따라 상태별 투표 목록 필터링
        state = params.get('state', None)
        if state == Vote.StateOfVote.ONGOING:
            queryset = ongoing_votes
        elif state == Vote.StateOfVote.FINISHED:
            queryset = finished_votes

        serializer = VoteSerializer(queryset, many=True, context={'user': request.user})
        data = {
            'ongoing_count': ongoing_votes.count(),
            'finished_count': finished_votes.count(),
            'votes': serializer.data
        }
        return data

    @action(methods=['get'], detail=False, url_path='created-votes')
    def created_votes(self, request):
        queryset = request.user.created_votes.all()
        data = self.list_my_page_votes(queryset, request)
        return Response(data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path='participated-votes')
    def participated_votes(self, request):
        queryset = request.user.participated_votes.all()
        data = self.list_my_page_votes(queryset, request)
        return Response(data, status=status.HTTP_200_OK)
