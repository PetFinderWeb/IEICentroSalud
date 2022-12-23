import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
import xml.etree.ElementTree as ET
import xmltodict
from appcore.extractors.extractor import Extractor
import json
from appcore.webScrapper.webScrapper import WebScrapper


class XML_Extactor(Extractor):
    webScrapper: WebScrapper

    def __init__(self):
        self.webScrapper = WebScrapper()

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
        self.latlangcode = self.webScrapper.searchByCoordinates(
            centro["lat"], centro["long"])
        if (self.latlangcode == None):
            return None
        else:
            return self.latlangcode

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["long"]

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["lat"]

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return "None"

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return "None"
