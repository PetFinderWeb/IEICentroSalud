
import csv
import os
from typing import *
# from CentroSaludCore.appcore.extractors.extractor import Extractor

from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor


class CSV_Extractor(Extractor):
    def abrir_fichero(self, path=os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv')):
        return open(path, mode='r')

    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        res = csv.DictReader(file, delimiter=';')
        print(res)
        return res