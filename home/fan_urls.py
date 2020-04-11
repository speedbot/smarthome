from django.urls import path

from home.views import FanCreateView, FanDeleteView, FanUpdateView, FanDetailView

urlpatterns = [
    path('create/', FanCreateView.as_view(), name='fan-create'),
    path('delete/<pk>/', FanDeleteView.as_view(), name='fan-delete'),
    path('update/<pk>/', FanUpdateView.as_view(), name='fan-update'),
    path('detail/<pk>/', FanDetailView.as_view(), name='bulb-detail'),
]