
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
from extractor import Extractor
import xml.etree.ElementTree as ET
import xmltodict
import json


class XML_Extactor(Extractor):

    

    def abrir_fichero(self, path: str = os.path.join(MEDIA_ROOT, 'biblioteques.xml')) -> IO:
        return open(path, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        xmldict = xmltodict.parse(file)
        xmlJson = json.dumps(xmldict)   



