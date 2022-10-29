
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
import xml.etree.ElementTree as ET
import xmltodict
from appcore.extractors.extractor import Extractor
import json


class XML_Extactor(Extractor):

    def abrir_fichero(self) -> IO:
        path = os.path.join(MEDIA_ROOT, 'biblioteques.xml')
        return open(path, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        xmldict = xmltodict.parse(file)
        xmlJson = json.dumps(xmldict)   



