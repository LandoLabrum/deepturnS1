from django.urls import path
from . import views

urlpatterns = [
    path('', views.one_view, name="form_one"),
]