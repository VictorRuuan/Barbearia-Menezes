from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('dados/', views.dados, name='dados'),
    path('servicos/', views.servicos, name='servicos'),
    path('calendario/', views.calendario, name='calendario'),
    path('confirmar/', views.confirmar, name='confirmar'),
    path('finalizar/', views.finalizar, name='finalizar'),
]
