from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id',
                  'nickname',
                  'profile_img',
                  'is_default_profile']
