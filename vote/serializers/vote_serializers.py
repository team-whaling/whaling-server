import requests
import pytz
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from vote.models import Vote, Choice, Coin
from .coin_serializers import CoinSerializer

COIN_SERVER_API = 'http://ec2-54-180-155-20.ap-northeast-2.compute.amazonaws.com/coins'


# 현재 코인 가격을 반환하는 함수
# ticker: 코인 코드(ex. BTC, ETH)
def get_coin_cur_price(ticker):
    params = {'coin_code': ticker}
    response = requests.get(COIN_SERVER_API, params=params).json()
    return response[0]['cur_price']


# 현재 시각을 반환하는 함수
def get_current_time():
    return datetime.now(pytz.timezone('Asia/Seoul')).replace(microsecond=0, second=0)


class VoteCreateSerializer(serializers.ModelSerializer):
    uploader = serializers.HiddenField(label='투표를 생성한 유저', default=serializers.CurrentUserDefault())
    coin_code = serializers.CharField()

    class Meta:
        model = Vote
        fields = [
            'vote_id',
            'uploader',
            'coin_code',
            'duration',
            'range',
            'comment',
        ]

    def validate(self, data):
        try:
            data['coin'] = Coin.objects.get(pk=data['coin_code'])
        except Coin.DoesNotExist:
            raise serializers.ValidationError({'coin_code': '지원하지 않는 코인입니다.'})
        return data

    def create(self, validated_data):
        # 투표 종료 시점, 트래킹 시점 설정
        current_time = get_current_time()
        if validated_data['duration'] == Vote.DurationOfQuestion.DAY:
            delta_finish = timedelta(hours=8)
            delta_track = timedelta(days=1)
        elif validated_data['duration'] == Vote.DurationOfQuestion.WEEK:
            delta_finish = timedelta(days=3)
            delta_track = timedelta(weeks=1)
        else:
            delta_finish = timedelta(weeks=1)
            delta_track = relativedelta(months=1)

        validated_data['finished_at'] = current_time + delta_finish
        validated_data['tracked_at'] = current_time + delta_track

        # 코인 정보 추가
        coin_code = validated_data.pop('coin_code')
        validated_data['created_price'] = get_coin_cur_price(coin_code)

        # 지급/차감 고래밥 개수 설정
        if self.context['request'].user.is_staff:
            validated_data['spent_point'] = 0
            validated_data['earned_point'] = 30

        return super().create(validated_data)


class VoteListSerializer(serializers.ModelSerializer):
    coin = CoinSerializer()

    class Meta:
        model = Vote
        fields = [
            'vote_id',
            'coin',
            'participants',
            'state',
            'finished_at',
            'earned_point',
            'duration',
            'range',
            'comment',
            'total_participants',
        ]


class VoteDetailSerializer(serializers.ModelSerializer):
    coin = CoinSerializer()
    is_admin_vote = serializers.SerializerMethodField(label='운영자 투표 여부', read_only=True,
                                                      method_name='get_admin_vote')

    class Meta:
        model = Vote
        exclude = ['participants']

    def get_admin_vote(self, obj):
        return obj.uploader.is_staff
