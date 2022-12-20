
from typing import *
from ..models import Establecimiento_Sanitario, Provincia, Localidad
from abc import ABC, abstractmethod


class Extractor(ABC):

    def extraer_de_fichero(self) -> None:
        archivo = self.abrir_fichero()
        datos = self.analizar_datos(archivo)
        self.guardar_datos(datos)
        archivo.close()

    @abstractmethod
    def abrir_fichero(self, ruta: str) -> IO:
        pass

    @abstractmethod
    def analizar_datos(self, file: IO) -> List[Dict[str, Any]]:
        pass

    def guardar_datos(self, mapped_data: List[Dict[str, Any]]) -> None:
        for centro in mapped_data:
            provincia = self.get_save_provincia(centro)
            localidad = self.get_save_localidad(centro, provincia)
            self.create_save_establecimiento_sanitario(centro, localidad)

    def get_save_provincia(self, centro: Dict[str, Any]) -> Provincia:
        try:
            provincia = Provincia.objects.get(
                nombre__exact=self.map_nombre_provincia(centro)
            )
        except Provincia.DoesNotExist:
            provincia = Provincia(
                nombre=self.map_nombre_provincia(centro),
            )
            provincia.save()
        return provincia

    def get_save_localidad(self, centro: Dict[str, Any], provincia: Provincia) -> Localidad:
        try:
            localidad = Localidad.objects.get(
                nombre__exact=self.map_nombre_localidad(centro),
            )
        except Localidad.DoesNotExist:
            localidad = Localidad(
                nombre=self.map_nombre_localidad(centro),
                en_provincia=provincia,
            )
            localidad.save()
        return localidad

    def create_save_establecimiento_sanitario(self, centro: Dict[str, Any], localidad: Localidad):
        centro = Establecimiento_Sanitario(
            nombre=self.map_nombre_establecimiento_sanitario(centro),
            tipo=self.map_tipo_establecimiento_sanitario(centro),
            direccion=self.map_direccion_establecimiento_sanitario(centro),
            longitud=self.map_longitud_establecimiento_sanitario(centro),
            latitud=self.map_latitud_establecimiento_sanitario(centro),
            codigo_postal=self.map_codigopostal_establecimiento_sanitario(centro),
            telefono=self.map_telefono_establecimiento_sanitario(centro),
            descripcion=self.map_descripcion_establecimiento_sanitario(centro),
            en_localidad=localidad
        )
        centro.save()

    @abstractmethod
    def map_nombre_provincia(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_nombre_localidad(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_nombre_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_tipo_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_direccion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_codigopostal_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_longitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        pass

    @abstractmethod
    def map_latitud_establecimiento_sanitario(self, centro: Dict[str, Any]) -> float:
        pass

    @abstractmethod
    def map_telefono_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def map_descripcion_establecimiento_sanitario(self, centro: Dict[str, Any]) -> str:
        pass
