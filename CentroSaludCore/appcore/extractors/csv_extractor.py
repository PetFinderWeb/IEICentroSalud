
from typing import *
# from CentroSaludCore.appcore.extractors.extractor import Extractor

from CentroSaludCore.settings import MEDIA_ROOT

from appcore.extractors.extractor import Extractor

from appcore.webScrapper.webScrapper import WebScrapper


class CSV_Extractor(Extractor):
    webScrapper: WebScrapper

    def __init__(self):
        self.webScrapper = WebScrapper()
        self.errores = []
        self.centrosSantinarios = 0

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
            res = "C"
        elif tipoCentro in tiposHospitales:
            res = "H"
        else:
            res = "O"
        return res

    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["Adreça / Dirección"]

    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        # Obtener mediante Web Scrapping
        if (len(self.latlang) == 3 and self.latlang[2] != None):
            return self.latlang[2]
        else:
            postalCode = self.webScrapper.searchByCoordinates(
                self.latlang[0], self.latlang[1])
            if (postalCode == None):
                raise Exception("No se ha podido obtener el código postal del centro sanitario " +
                                self.map_nombre_establecimiento_sanitario(centro))
            else:
                return postalCode

    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtener mediante Web Scrapping
        self.latlang = self.webScrapper.searchByAddress(
            centro["Adreça / Dirección"] + " , " + centro["Municipi / Municipio"] + ', ESPAÑA')

        if (self.latlang[1] == None):
            raise Exception("No se ha podido obtener la longitud del centro sanitario " +
                            self.map_nombre_establecimiento_sanitario(centro))
        else:
            return self.latlang[1]

    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        # Obtenido mediante web scrapping en el método map_longitud_establecimiento_sanitario
        if (self.latlang[0] == None):
            raise Exception("No se ha podido obtener la latitud del centro sanitario " +
                            self.map_nombre_establecimiento_sanitario(centro))
        else:
            return self.latlang[0]

    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return None  # No tenemos teléfono

    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        return centro["Tipus_centre / Tipo_centro"] + ' | ' + centro["Règim /Régimen"]
