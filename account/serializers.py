from email._header_value_parser import get_address

from rest_framework import serializers
from django.contrib.auth import get_user_model

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
