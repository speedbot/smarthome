from rest_framework.viewsets import ModelViewSet

from .models import Bulb, Fan

from .serializiers import FanSerializer, BulbSerializer


class BulbViewSet(ModelViewSet):
    queryset = Bulb.objects.filter()
    serializer_class = BulbSerializer


class FanViewSet(ModelViewSet):
    queryset = Fan.objects.filter()
    serializer_class = FanSerializer
