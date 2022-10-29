
import csv
import os
from typing import *
# from CentroSaludCore.appcore.extractors.extractor import Extractor

from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor


class CSV_Extractor(Extractor):
    def abrir_fichero(self):
        path = os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv')
        print('hola')
        return open(path, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        res = csv.DictReader(file, delimiter=';')
        print(res)
        return res
    
    def map_codigo_provincia(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_codigo_localidad(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        pass
    
    
    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        pass

    
    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        pass

    
    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    
    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass