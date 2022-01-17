from datetime import datetime, timedelta

import pytz
from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from .models import *


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


class VoteCreateSerializer(serializers.ModelSerializer):
    uploader = serializers.HiddenField(label='투표를 생성한 유저', default=serializers.CurrentUserDefault())

    class Meta:
        model = Vote
        fields = [
            'vote_id',
            'uploader',
            # 'coin',
            'finished_at',
            'tracked_at',
            'created_price',
            'spent_point',
            'earned_point',
            'duration',
            'range',
            'comment',
        ]
        read_only_fields = [
            'finished_at',
            'tracked_at',
            'created_price',
            'spent_point',
            'earned_point',
        ]

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

        # 코인 서버 연결
        validated_data['created_price'] = 1000

        # 지급/차감 고래밥 개수 설정
        if self.context['request'].user.is_staff:
            validated_data['spent_point'] = 0
            validated_data['earned_point'] = 30

        return super().create(validated_data)


class VoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = [
            'vote_id',
            # 'coin',
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
    is_admin_vote = serializers.SerializerMethodField(label='운영자 투표 여부', read_only=True,
                                                      method_name='get_admin_vote')
    choice = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Vote
        exclude = ['participants']

    def get_admin_vote(self, obj):
        return obj.uploader.is_staff

    def get_choice(self, obj):
        user = self.context.get("request").user
        try:
            choice_data = Choice.objects.get(vote_id=obj.vote_id, participant_id=user.user_id)
            return choice_data.choice
        except Choice.DoesNotExist:
            return None
