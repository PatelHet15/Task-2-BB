# cars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add/', views.car_form, name='car_form'), 
    path('success/', views.car_success, name='car_success'),  
]
