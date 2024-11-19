from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calc, name="home"),
    path('submit', views.calc, name='submit'),
]