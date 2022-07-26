from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.valida_e_salva_link, name='valida_link'),
    path('<str:link>/', views.redirecionar, name='redirecionar'),
]
