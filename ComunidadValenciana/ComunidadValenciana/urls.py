"""ComunidadValenciana URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # el endpoint del wrapper se encuentra definito en wrapper.urls
    path('wrapper/', include('wrapper.urls'))
]
