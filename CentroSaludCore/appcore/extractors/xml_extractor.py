
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
import xml.etree.ElementTree as ET
import xmltodict
import pprint
from appcore.extractors.extractor import Extractor
import json


class XML_Extactor(Extractor):

    def abrir_fichero(self, path: str = os.path.join(MEDIA_ROOT, 'biblioteques.xml')) -> IO:
        return open(path, mode='r', encoding='utf-8')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        xmldict = xmltodict.parse(file.read())
        xmlJson = json.dumps(xmldict, ensure_ascii=False)
        json_object = json.loads(xmlJson)
        return json_object['response']['row']['row']

    
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

    # with open(os.path.join(MEDIA_ROOT, 'biblioteques.xml')) as fd:
    #     doc = xmltodict.parse(fd.read())

    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(json.dumps(doc))

    # print(pp)