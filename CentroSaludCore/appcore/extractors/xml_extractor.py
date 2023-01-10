import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
import xml.etree.ElementTree as ET
from appcore.extractors.extractor import Extractor
from appcore.webScrapper.webScrapper import WebScrapper

"""Clase que representa el Extractor de la las islas baleares, extiende de la clase 
extractor e implementa los métodos abstractos."""


class XML_Extactor(Extractor):
    webScrapper: WebScrapper

    # Constructor de la clase. Instancia el webScrapper
    def __init__(self):
        self.webScrapper = WebScrapper()
        self.errores = []
        self.centrosSantinarios = 0

    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return "Islas baleares"

    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        return centro["municipi"]

    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["nom"]

    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipoCentro = centro["funcio"]
        if tipoCentro == "CENTRE SANITARI" or tipoCentro == "UNITAT BÀSICA":
            res = "C"
        else:
            res = "O"
        return res

    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["adreca"]

    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        # Obtener mediante Web Scrapping el código postal a partir de la latitud y longitud
        self.latlangcode = self.webScrapper.searchByCoordinates(
            centro["lat"], centro["long"])
        # Comprobar si se ha podido obtener el código postal. EN caso negativo desechar registro
        if (self.latlangcode == None):
            raise Exception("No se ha podido obtener el código postal del centro sanitario " +
                            self.map_nombre_establecimiento_sanitario(centro))
        else:
            return self.latlangcode

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["long"]

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["lat"]

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return "None"  # No tenemos teléfono

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return "None"
