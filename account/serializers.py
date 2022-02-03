from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id',
                  'nickname',
                  'profile_img',
                  'is_default_profile']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'nickname',
            'acc_percent',
            'point',
            'profile_img',
            'is_default_profile'
        ]


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    access_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        refresh_token = RefreshToken(attrs['refresh_token'])
        data = {
            'access_token': str(refresh_token.access_token)
        }
        return data
