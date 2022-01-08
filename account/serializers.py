from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['user_id',
        #           'email',
        #           'nickname',
        #           'profile_img',
        #           'is_default_profile']
        fields = '__all__'
