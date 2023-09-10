from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('index/connect', views.connect_drone, name='connect'),
]