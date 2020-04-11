from django.urls import path

from home.views import BulbCreateView, BulbUpdateView, BulbDeleteView, BulbDetailView

urlpatterns = [
    path('create/', BulbCreateView.as_view(), name='bulb-create'),
    path('update/<pk>/', BulbUpdateView.as_view(), name='bulb-update'),
    path('delete/<pk>/', BulbDeleteView.as_view(), name='bulb-delete'),
    path('detail/<pk>/', BulbDetailView.as_view(), name='bulb-detail'),
]