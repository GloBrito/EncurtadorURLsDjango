from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('valida_link/', views.valida_link, name='valida_link'),
    
]

