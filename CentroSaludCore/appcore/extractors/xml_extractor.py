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

    def abrir_fichero(self, path: str = os.path.join(MEDIA_ROOT, 'biblioteques.xml')) -> IO:
        return open(path, mode='r', encoding='utf-8')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        xmldict = xmltodict.parse(file.read())
        xmlJson = json.dumps(xmldict, ensure_ascii=False)
        json_object = json.loads(xmlJson)
        return json_object['response']['row']['row']

    def map_codigo_provincia(self, centro: Dict[str, Any]) -> str:
        return "07"

    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        return "Islas baleares"

    def map_codigo_localidad(self, centro: Dict[str, Any]) -> str:
        return ""

    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        return centro["municipi"]

    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["nom"]

    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        tipoCentro = centro["funcio"]
        if tipoCentro == "CENTRE SANITARI" or tipoCentro == "UNITAT BÀSICA":
            res = "CENTRO DE SALUD"
        else:
            res = "OTROS"
        return res

    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["adreca"]

    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        self.latlangcode = self.webScrapper.searchByCoordinates(
            self, centro["lat"], centro["long"])
        if (self.latlangcode == None):
            return None
        else:
            return self.latlangcode

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["long"]

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        return centro["lat"]

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return None

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return None
