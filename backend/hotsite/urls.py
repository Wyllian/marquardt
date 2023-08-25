from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'hotsite'
urlpatterns = [
    path('', views.index, name='index'),
]
