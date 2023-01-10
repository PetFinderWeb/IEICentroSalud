"""IslasBaleares URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # en wrapper.urls se detalla el endpoint del wrapper
    path('wrapper/', include('wrapper.urls'))
]
