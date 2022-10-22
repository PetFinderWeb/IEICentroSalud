from django.urls import path

from . import views

urlpatterns = [
    path('cargar_csv/', views.cargar_csv, name='csv'),
    path('cargar_xml/', views.cargar_xml, name='xml'),
    path('cargar_json/', views.cargar_json, name='json'),
]