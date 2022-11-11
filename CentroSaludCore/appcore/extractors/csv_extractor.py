
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
        
        # Crea el archivo json
        # with open(os.path.join(MEDIA_ROOT, 'DataExtractorCSV.json'), 'w', encoding='utf-8') as jsonf: 
        #     jsonString = json.dumps(jsonDatos, indent=4, ensure_ascii=False)
        #     print(jsonString[0])
        #     jsonf.write(jsonString)
        return jsonDatos
    
    def map_codigo_provincia(self, centro: Dict[str, Any]) -> str:
        return centro["Codi_província / Código_provincia"]

    
    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
         return centro["Província / Provincia"]

    
    def map_codigo_localidad(self, centro: Dict[str, Any]) -> str:
        return "CV"+ centro["Codi_municipi / Código_municipio"]
    
    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
         return centro["Municipi / Municipio"]
    
    
    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
       return centro["Centre / Centro"]

    
    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipoCentro = centro["Tipus_centre / Tipo_centro"]
        tiposCentrosDeSalud = [
            'CENTRO/SERVICIO DE URGENCIAS Y EMERGENCIAS',
            'CENTROS DE CIRUGIA MAYOR AMBULATORIA',
            'CENTROS DE ESPECIALIDADES',
            'CENTROS DE SALUD', 
            'CENTROS DE SALUD MENTAL',
            'CENTROS POLIVALENTES',
            'CONSULTORIOS DE ATENCIÓN PRIMARIA'
        ]
        tiposHospitales = [
            'HOSPITALES DE SALUD MENTAL Y TRATAMIENTO DE TOXICOMANÍAS',
            'HOSPITALES DE MEDIA Y LARGA ESTANCIA',
            'HOSPITALES ESPECIALIZADOS',
            'HOSPITALES GENERALES'
        ]
        if tipoCentro in tiposCentrosDeSalud: # Añadir el resto de tipos de centros
            res = "CENTRO DE SALUD"
        elif tipoCentro in tiposHospitales:
            res = "HOSPITAL"
        else:
            res = "OTROS"
        return res

        
    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["Adreça / Dirección"]

    
    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        # Obtener mediante Web Scrapping
        return centro["Codi_província / Código_provincia"] + centro["Codi_municipi / Código_municipio"]

    
    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtener mediante Web Scrapping
        return 3.59876

    
    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtener mediante Web Scrapping
        return 43.59876

    
    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return None # No tenemos teléfono

    
    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["Tipus_centre / Tipo_centro"] + ' | ' + centro["Règim /Régimen"]