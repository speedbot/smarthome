from django.urls import path

from home.views import BulbCreateView, BulbUpdateView, BulbDeleteView, BulbDetailView

app_name='bulb'
urlpatterns = [
    path('create/', BulbCreateView.as_view(), name='create'),
    path('update/<pk>/', BulbUpdateView.as_view(), name='update'),
    path('delete/<pk>/', BulbDeleteView.as_view(), name='delete'),
    path('detail/<pk>/', BulbDetailView.as_view(), name='detail'),
]