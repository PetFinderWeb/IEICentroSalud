from django.urls import path

from . import views

urlpatterns = [
    path('cargar_csv/', views.cargar_csv, name='csv'),
    path('cargar_xml/', views.cargar_xml, name='xml'),
    path('cargar_json/', views.cargar_json, name='json'),
    path('borrar_bdd/', views.borrar_bdd, name='borrar_bdd'),
    path('carga_parametrizada/', views.carga_parametrizada, name='carga_parametrizada'),
    path('busqueda/', views.busqueda, name='busqueda'),
]