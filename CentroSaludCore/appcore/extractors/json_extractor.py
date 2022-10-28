import json
import os
from typing import *

from CentroSaludCore.settings import MEDIA_ROOT

from extractor import Extractor



class JSON_Extractor(Extractor):

    def abrir_fichero(self, path=os.path.join(MEDIA_ROOT, 'bibliotecas.json')):
        return open(path, mode='r')

    def analizar_datos(self, file):
        return json.load(file)
    
    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return centro.get('Provincia').strip().title()
    
    def map_codigo_provincia(self, centro: Dict[str, Any]) -> str:
        return centro.get('Codigopostal')[0:2]
    
    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        return centro.get('Municipio').strip().title()

    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro.get('Nombre')

    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipo = centro.get('Tipodecentro').strip().lowercase()
        if 'centro de salud' in tipo:
            
    
    # ...