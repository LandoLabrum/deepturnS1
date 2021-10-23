# from django.contrib.auth import views as auth_views
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormOne, name="form-one"),
]
