from django.urls import path ,include
from .views import register_view,logout_confirm
from django.contrib.auth.views import  LogoutView, LoginView


urlpatterns=[
    path('register/', register_view, name='register'),
    path('logout-confirm/', logout_confirm, name='logout-confirm'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]