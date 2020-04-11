from django.contrib.auth import views as auth_views
from django.urls import  path

from home.views import Home

app_name='accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'login.html', 'success_url': ''}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'template_name': 'logout.html'}, name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', Home.as_view()),
]
