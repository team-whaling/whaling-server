from rest_framework import serializers

from vote.models import Choice


class ChoiceSerializer(serializers.ModelSerializer):
    participant = serializers.HiddenField(label='투표에 참여한 유저', default=serializers.CurrentUserDefault())

    class Meta:
        model = Choice
        fields = '__all__'

    def validate(self, data):
        if self.context['request'].user == data['vote'].uploader:
            raise serializers.ValidationError({'participant': '투표 생성자는 투표에 참여할 수 없습니다.'})
        return data
