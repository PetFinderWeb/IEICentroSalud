import json
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor

"""Clase que representa el Extractor del país vasco, extiende de la clase 
extractor e implementa los métodos abstractos."""


class JSON_Extractor(Extractor):

    def __init__(self):
        self.errores = []
        self.centrosSantinarios = 0

    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Nombre')

    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipo = centro.get('Tipodecentro').strip().lower()
        if 'centro de salud' == tipo or 'consultorio' == tipo or 'ambulatorio' == tipo or 'centro de salud mental' == tipo:
            return 'C'
        if 'hospital' == tipo:
            return 'H'
        else:
            return 'O'

    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Direccion').strip()

    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Codigopostal').strip()

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return float(centro.get('LATWGS84'))

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return float(centro.get('LONWGS84'))

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        # Eliminar los puntos y algunos teléfonos que tienen ',0' final
        return centro.get('Telefono', '').strip().replace(',0', '').replace('.', '')

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        horario = centro.get('HorarioatencionCiudadana')
        # Si tenemos información sobre el horario del centro lo ponemos como descripción
        if horario is not None:
            return horario
        else:
            return 'Horario no disponible'

    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        return centro.get('Municipio').strip().title()

    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return centro.get('Provincia').strip().title()
