from rest_framework import serializers

from vote.models import Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        exclude = ['name']
