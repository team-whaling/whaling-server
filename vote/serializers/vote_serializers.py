import requests
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from account.models import get_current_time
from vote.models import Vote, Coin, Choice
from vote.serializers import CoinSerializer
from whaling.settings import env


# 현재 코인 가격을 반환하는 함수
# ticker: 코인 코드(ex. BTC, ETH)
def get_coin_cur_price(ticker):
    params = {'coin_code': ticker}
    response = requests.get(env('COIN_SERVER_API'), params=params).json()
    return response[0]['cur_price']


# 투표 상세 정보 조회
class VoteSerializer(serializers.ModelSerializer):
    coin = CoinSerializer()
    is_admin_vote = serializers.SerializerMethodField(label='운영자 투표 여부', read_only=True,
                                                      method_name='get_admin_vote')

    class Meta:
        model = Vote
        exclude = ['participants']

    def get_admin_vote(self, obj):
        return obj.uploader.is_staff

    def to_representation(self, instance):
        # 응답 데이터에 현재 로그인 유저의 투표 참여 정보 추가
        data = super().to_representation(instance)
        vote_id = data['vote_id']
        user_id = self.context['user'].user_id
        try:
            choice_obj = Choice.objects.get(vote_id=vote_id, participant_id=user_id)
            choice = choice_obj.choice
            is_answer = choice_obj.is_answer
            participated_at = choice_obj.created_at
        except Choice.DoesNotExist:
            choice = is_answer = participated_at = None
        data['user'] = {
            'choice': choice,
            'is_answer': is_answer,
            'participated_at': participated_at
        }
        return data


# 투표 생성
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

        if data['range'] <= 0 or data['range'] > 300:
            raise serializers.ValidationError({'range': '예상 변동폭이 생성 가능한 범위를 초과했습니다.'})

        user = self.context['request'].user
        if not user.is_staff and user.point < 50:
            raise serializers.ValidationError({'uploader': '고래밥이 부족합니다.'})

        return data

    def create(self, validated_data):
        # 투표 종료 시점, 트래킹 시점 설정
        current_time = get_current_time().replace(microsecond=0, second=0)
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

        user = self.context['request'].user
        if user.is_staff:
            # 운영자 생성 투표인 경우 지급/차감 고래밥 개수 변경
            validated_data['spent_point'] = 0
            validated_data['earned_point'] = 30
        else:
            # 운영자가 아닌 유저는 투표 생성 시 고래밥 차감
            user.point -= 50
            user.save()

        return super().create(validated_data)
