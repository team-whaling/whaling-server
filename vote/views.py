from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets, status, filters, permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Vote, Coin
from .serializers import vote_serializers, choice_serializers


class VoteViewSet(viewsets.GenericViewSet):
    queryset = Vote.objects.exclude(state=Vote.StateOfVote.TRACKED)
    serializer_class = vote_serializers.VoteCreateSerializer

    def get_filtered_queryset(self, params):
        queryset = self.get_queryset()
        state = params.get('state', None)
        sort = params.get('sort', None)
        coin = params.get('coin', None)
        if state in Vote.StateOfVote:
            queryset = queryset.filter(state=state)
        if sort == 'popular':
            queryset = queryset.order_by('-total_participants')
        if coin is not None:
            queryset = queryset.filter(Q(coin__code__icontains=coin) | Q(coin__krname__icontains=coin))
        return queryset

    def list(self, request):
        queryset = self.get_filtered_queryset(request.query_params)
        serializer = vote_serializers.VoteListSerializer(
            queryset,
            many=True,
            context={'user': request.user}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        vote = get_object_or_404(queryset, pk=pk)
        serializer = vote_serializers.VoteDetailSerializer(vote, context={'user': request.user})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        vote = serializer.save()
        data = {
            'vote_id': vote.vote_id
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def choice(self, request, pk=None):
        request.data['vote'] = pk
        serializer = choice_serializers.ChoiceSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def acc_percent_of_whaling(request):
    total_votes = Vote.objects.all().count()
    correct_votes = Vote.objects.filter(is_answer=True).count()
    acc_percent = (correct_votes / total_votes) * 100
    data = {
        'acc_percent': format(acc_percent, '.1f')
    }
    return Response(data, status=status.HTTP_200_OK)


class CoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = vote_serializers.CoinSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['code', 'krname']
