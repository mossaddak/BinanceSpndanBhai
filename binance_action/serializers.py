from rest_framework import serializers


class BinanceConnectSerializer(serializers.Serializer):
    binance_api_key = serializers.CharField()
    binance_api_secrect = serializers.CharField()