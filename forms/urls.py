from django.urls import path
from . import views

urlpatterns = [
    path('', views.F101View),
]