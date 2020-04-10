from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from .viewsets import BulbViewSet, FanViewSet

router = routers.DefaultRouter()
router.register(r'fan', FanViewSet)
router.register(r'bulb', BulbViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
]
