from django.urls import path

from . import views

urlpatterns = [
    # endpoint del wrapper
    path('cargar_csv/', views.cargar_csv, name='csv'),
]
