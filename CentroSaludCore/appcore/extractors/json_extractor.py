import json
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor



class JSON_Extractor(Extractor):

    def abrir_fichero(self):
        path = os.path.join(MEDIA_ROOT, 'bibliotecas.json')
        return open(path, mode='r', encoding="utf8")

    def analizar_datos(self, file):
        return json.load(file)

    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Nombre')

    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipo = centro.get('Tipodecentro').strip().lower()
        if 'centro de salud' in tipo:
            return 'CENTRO DE SALUD'
        if 'hospital' in tipo:
            return 'HOSPITAL'
        else:
            return 'OTROS'
        
    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Direccion').strip()
    
    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Codigopostal').strip()
    
    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return float(centro.get('LATWGS84'))
        
    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return float(centro.get('LONWGS84'))
    
    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Telefono', '').strip().replace(',0', '').replace('.', '')

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        horario = centro.get('HorarioatencionCiudadana')
        if horario is not None: 
            return horario
        else:
            return 'Horario no disponible'

    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        return centro.get('Municipio').strip().title()
    
    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return centro.get('Provincia').strip().title()
