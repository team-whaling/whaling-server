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
        if data['participant'] == data['vote'].uploader:
            raise serializers.ValidationError({'participant': '투표 생성자는 투표에 참여할 수 없습니다.'})
        return data

    def create(self, validated_data):
        vote = validated_data['vote']
        is_whale = (validated_data['participant'].acc_percent >= 70)
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
        return super().create(validated_data)

    def to_representation(self, instance):
        data = {
            'vote_id': instance.vote_id,
            'choice': instance.choice
        }
        return data
