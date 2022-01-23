from functools import partial

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from vote.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    participant = serializers.HiddenField(label='투표에 참여한 유저', default=serializers.CurrentUserDefault())

    class Meta:
        model = Choice
        fields = [
            'vote',
            'participant',
            'choice'
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Choice.objects.all(),
                fields=['vote', 'participant'],
                message='이미 참여한 투표입니다.'
            )
        ]

    def validate(self, data):
        vote = data['vote']
        participant = data['participant']

        if participant.point < vote.spent_point:
            raise serializers.ValidationError({'participant': '고래밥이 부족합니다.'})
        return data

    def create(self, validated_data):
        vote = validated_data['vote']
        participant = validated_data['participant']
        is_whale = (participant.acc_percent >= 70)
        choice = validated_data['choice']

        # 투표 참여자 수 증가
        vote.total_participants += 1
        if choice == Choice.ChoiceOfVote.YES:
            vote.pos_participants += 1
            if is_whale:
                vote.pos_whales += 1
        else:
            vote.neg_participants += 1
            if is_whale:
                vote.neg_whales += 1
        vote.save()

        # 유저 고래밥 차감
        participant.point -= vote.spent_point
        participant.save()
        return super().create(validated_data)

    def to_representation(self, instance):
        data = {
            'vote_id': instance.vote_id,
            'choice': instance.choice
        }
        return data
