from django.urls import path

from . import views

urlpatterns = [
    # endpoint para borrar la base de datos
    path('borrar_bdd/', views.borrar_bdd, name='borrar_bdd'),
    # endpoint para poblar el warehouse
    path('carga_parametrizada/', views.carga_parametrizada,
         name='carga_parametrizada'),
    # endpoint para realizar consultas al warehouse
    path('busqueda/', views.busqueda, name='busqueda'),
]
