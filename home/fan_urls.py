from django.urls import path

from home.views import FanCreateView, FanDeleteView, FanUpdateView, FanDetailView

app_name='fan'
urlpatterns = [
    path('create/', FanCreateView.as_view(), name='create'),
    path('delete/<pk>/', FanDeleteView.as_view(), name='delete'),
    path('update/<pk>/', FanUpdateView.as_view(), name='update'),
    path('detail/<pk>/', FanDetailView.as_view(), name='detail'),
]