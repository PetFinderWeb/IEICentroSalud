from django.urls import path

from . import views

urlpatterns = [
    # Endpoint del wrapper de las islas baleares
    path('cargar_xml/', views.cargar_xml, name='xml'),
]
