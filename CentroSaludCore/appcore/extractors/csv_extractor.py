
import codecs
import csv
import os
import json
from typing import *
# from CentroSaludCore.appcore.extractors.extractor import Extractor

from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor

from appcore.webScrapper.webScrapper import WebScrapper

class CSV_Extractor(Extractor):
    def __init__(self):
            self.webScrapper = WebScrapper()

    def abrir_fichero(self, ruta=os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv')):
        return open(ruta, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        jsonDatos = []
        # CSV to JSON
        datosDiccionario = csv.DictReader(file, delimiter=';')
        for row in datosDiccionario:
            jsonDatos.append(row)
        return jsonDatos

    def map_codigo_provincia(self, centro: Dict[str, Any]) -> str:
        return centro["Codi_província / Código_provincia"]

    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return centro["Província / Provincia"]

    def map_codigo_localidad(self, centro: Dict[str, Any]) -> str:
        return "CV" + centro["Codi_municipi / Código_municipio"]

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
        if tipoCentro in tiposCentrosDeSalud:  # Añadir el resto de tipos de centros
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
        self.latlangcode = self.webScrapper.searchByAddress(centro["Adreça / Dirección"] + " , " + centro["Municipi / Municipio"] + ', ESPAÑA')
        if (self.latlangcode[2] == None): 
            return None
        else:
            return self.latlangcode[2]

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtener mediante Web Scrapping
        return self.latlangcode[1]

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtener mediante Web Scrapping
        return self.latlangcode[0]

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return None  # No tenemos teléfono

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["Tipus_centre / Tipo_centro"] + ' | ' + centro["Règim /Régimen"]
