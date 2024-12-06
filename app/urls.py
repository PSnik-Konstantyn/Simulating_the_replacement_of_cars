from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calc, name="home"),
    path('submit', views.calc, name='submit'),
    path('description', views.description, name='description'),
    path('trends', views.trends, name='trends'),
    path('about_dvz', views.about_dvz, name='about_dvz'),
    path('about_ev', views.about_ev, name='about_ev'),
]
