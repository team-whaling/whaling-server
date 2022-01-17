from datetime import datetime, timedelta

import pytz
from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from .models import *


class CurrentUserIdDefault(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.user_id


def get_current_time():
    return datetime.now(pytz.timezone('Asia/Seoul')).replace(microsecond=0, second=0)


class ChoiceSerializer(serializers.ModelSerializer):
    participant = serializers.HiddenField(label='투표에 참여한 유저', default=serializers.CurrentUserDefault())

    class Meta:
        model = Choice
        fields = '__all__'

    def validate(self, data):
        if self.context['request'].user == data['vote'].uploader:
            raise serializers.ValidationError({'participant': '투표 생성자는 투표에 참여할 수 없습니다.'})
        return data


class VoteSerializer(serializers.ModelSerializer):
    is_admin_vote = serializers.SerializerMethodField(label='운영자 투표 여부', read_only=True, method_name='get_admin_vote')
    uploader = serializers.HiddenField(label='투표를 생성한 유저', default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        exclude = ['participants']
        read_only_fields = [
            'finished_at',
            'tracked_at',
            'created_price',
            'finished_price',
            'spent_point',
            'earned_point',
            'is_answer',
            'pos_participants',
            'neg_participants',
            'pos_whales',
            'neg_whales',
        ]

    def get_admin_vote(self, obj):
        return obj.uploader.is_staff

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

        # 아직 코인 서버 연결 X
        validated_data['created_price'] = 1000

        return super().create(validated_data)
