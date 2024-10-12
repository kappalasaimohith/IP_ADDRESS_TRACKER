from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('track/', views.track_ip, name='track_ip'),
]
