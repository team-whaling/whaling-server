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
