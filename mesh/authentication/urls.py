from django.conf.urls import url
from django.urls import path,include

from knox.views import LogoutView

from .views import LoginAPIView,UserAPIView,registration_view

urlpatterns = [
    path('',include('knox.urls')),
    path('register',registration_view),
    path('user',UserAPIView.as_view()),
    path('login',LoginAPIView.as_view()),
    path('logout',LogoutView.as_view(),name='knox_logout'),
]