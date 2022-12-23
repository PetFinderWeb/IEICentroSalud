from django.urls import path

from . import views

urlpatterns = [
    path('cargar_csv/', views.cargar_csv, name='csv'),
]
