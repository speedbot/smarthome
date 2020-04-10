from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from django.contrib.auth import views as auth_views

from .views import BulbCreateView, FanCreateView, BulbDeleteView, FanDeleteView, BulbUpdateView, FanUpdateView, \
    BulbDetailView, FanDetailView, Home
from .viewsets import BulbViewSet, FanViewSet

router = routers.DefaultRouter()
router.register(r'fan', FanViewSet)
router.register(r'bulb', BulbViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/', include(router.urls)),
    path('login', auth_views.LoginView.as_view(), {'template_name':'login.html', 'success_url': ''}, name='login'),
    path('logout', auth_views.LogoutView.as_view(), {'template_name':'logout.html'}, name='logout'),
    path('home', Home.as_view(), name='home'),
    path('bulb/create', BulbCreateView.as_view(), name='bulb-create'),
    path('bulb/update/<pk>/', BulbUpdateView.as_view(), name='bulb-update'),
    path('bulb/delete/<pk>/', BulbDeleteView.as_view(), name='bulb-delete'),
    path('bulb/detail/<pk>/', BulbDetailView.as_view(), name='bulb-detail'),
    path('fan/create', FanCreateView.as_view(), name='fan-create'),
    path('fan/delete/<pk>/', FanDeleteView.as_view(), name='fan-delete'),
    path('fan/update/<pk>/', FanUpdateView.as_view(), name='fan-update'),
    path('fan/detail/<pk>/', FanDetailView.as_view(), name='bulb-detail'),
]
