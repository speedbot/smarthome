from .models import Bulb, Fan

from rest_framework.serializers import ModelSerializer


class BulbSerializer(ModelSerializer):
    class Meta:
        model = Bulb
        fields = ('owner', 'name', 'state', 'brightness', 'color')


class FanSerializer(ModelSerializer):
    class Meta:
        model = Fan
        fields = ('owner', 'name', 'state', 'speed')
