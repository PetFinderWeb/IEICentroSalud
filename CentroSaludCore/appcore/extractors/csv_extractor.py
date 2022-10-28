
import codecs
import csv
import os
import json
from typing import *
# from CentroSaludCore.appcore.extractors.extractor import Extractor

from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor


class CSV_Extractor(Extractor):
    def abrir_fichero(self, ruta=os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv')):
        print('hola')
        return open(ruta, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        jsonDatos=[]
        datosDiccionario = csv.DictReader(file, delimiter=';')
        for row in datosDiccionario:
            jsonDatos.append(row)
        with open(os.path.join(MEDIA_ROOT, 'DataExtractorCSV.json'), 'w', encoding='utf-8') as jsonf: 
            jsonString = json.dumps(jsonDatos, indent=4, ensure_ascii=False)
            print(jsonString[0])
            jsonf.write(jsonString)
        
        return jsonDatos
    
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