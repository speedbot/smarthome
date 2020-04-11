from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from .views import Home
from .viewsets import BulbViewSet, FanViewSet

router = routers.DefaultRouter()
router.register(r'fan', FanViewSet)
router.register(r'bulb', BulbViewSet)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('home.accounts_urls'), name='accounts'),
    path('bulb/', include('home.bulb_urls', namespace='bulb'), name='bulb'),
    path('fan/', include('home.fan_urls', namespace='fan'), name='fan'),

]
