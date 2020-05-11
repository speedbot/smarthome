from .models import Bulb, Fan

from rest_framework.serializers import ModelSerializer


class BulbSerializer(ModelSerializer):
    class Meta:
        model = Bulb
        fields = ('id','owner', 'name', 'state', 'brightness', 'color', 'get_absolute_url')


class FanSerializer(ModelSerializer):
    class Meta:
        model = Fan
        fields = ('id', 'owner', 'name', 'state', 'speed', 'get_absolute_url')
