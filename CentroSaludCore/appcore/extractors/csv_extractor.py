
import os

from CentroSaludCore.settings import MEDIA_ROOT

from extractor import Extractor


class CSV_Extractor(Extractor):
    def abrir_fichero(self, path=os.path.join(MEDIA_ROOT, 'directorio-de-bibliotecas-valencianas_2020.csv')):
        return open(path, mode='r')
