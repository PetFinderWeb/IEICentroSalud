from django.urls import path

from . import views

urlpatterns = [
    path('cargar_json/', views.cargar_json, name='json'),
]
