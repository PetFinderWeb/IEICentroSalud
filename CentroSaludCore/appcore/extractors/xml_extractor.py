
import os
from typing import *
from CentroSaludCore.settings import MEDIA_ROOT
from appcore.extractors.extractor import Extractor
import xml.etree.ElementTree as ET


class XML_Extactor(Extractor):

    def abrir_fichero(self, path: str = os.path.join(MEDIA_ROOT, 'biblioteques.xml')) -> IO:
        return open(path, mode='r')

