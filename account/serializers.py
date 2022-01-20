from rest_framework import serializers

from .models import User


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
