from django.urls import path

from . import views

urlpatterns = [
    # endpoint del wrapper de euskadi
    path('cargar_json/', views.cargar_json, name='json'),
]
