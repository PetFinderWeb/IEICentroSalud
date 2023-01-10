"""CentroSaludCore URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Conjunto de endpoints para inspeccionar la base de datos
    path('admin/', admin.site.urls),
    # Conjunto de endpoints para interactuar con la aplicación (carga de centros, búsqueda de centros
    # y borrado de la base de datos)
    path('core/', include('appcore.urls'))
]
