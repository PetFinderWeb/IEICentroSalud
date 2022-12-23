from django.urls import path

from . import views

urlpatterns = [
    path('cargar_xml/', views.cargar_xml, name='xml'),
]
