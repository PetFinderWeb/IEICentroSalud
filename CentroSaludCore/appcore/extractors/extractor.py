
from typing import *
from ..models import Establecimiento_Sanitario, Provincia, Localidad
from abc import ABC, abstractmethod
import http.client
import json


class Extractor(ABC):
    errores: List[str] = []
    centrosSantinarios: int = 0

    def extraer_de_fichero(self, port, path, server='localhost', all=False) -> List[str]:
        datos = self.llamar_wrapper(port, path, server, all)
        self.guardar_datos(datos)

    def llamar_wrapper(self, port, path, server, all):
        try:
            connection = http.client.HTTPConnection(server, port)
            if all == True:
                headers = {"all": "true"}
            else:
                headers = {}
            connection.request("GET", path, headers=headers)
            response = connection.getresponse()
            if response.status != 200:
                raise Exception(
                    "Status code " + str(response.status))
            string = response.read().decode('utf-8')
            json_content = json.loads(string)
            connection.close()
        except Exception as e:
            raise Exception("Error al comunicarse con el wrapper. " + str(e))
        return json_content

    def guardar_datos(self, mapped_data: List[Dict[str, Any]]) -> None:
        for centro in mapped_data:
            try:
                provincia = self.get_save_provincia(centro)
                localidad = self.get_save_localidad(centro, provincia)
                self.create_save_establecimiento_sanitario(centro, localidad)
                self.centrosSantinarios += 1
            except Exception as e:
                self.errores.append(str(e))
                continue

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
        nombre = self.map_nombre_establecimiento_sanitario(centro)
        # Comprobamos si el centro ya existe en la base de datos
        centroRepetido = Establecimiento_Sanitario.establecimientos.filter(
            nombre__iexact=nombre
        )
        if centroRepetido.count() != 0:
            raise Exception("El centro sanitario " +
                            nombre + " se encuentra repetido.")

        centro = Establecimiento_Sanitario(
            nombre=nombre,
            tipo=self.map_tipo_establecimiento_sanitario(centro),
            direccion=self.map_direccion_establecimiento_sanitario(centro),
            longitud=self.map_longitud_establecimiento_sanitario(centro),
            latitud=self.map_latitud_establecimiento_sanitario(centro),
            codigo_postal=self.map_codigopostal_establecimiento_sanitario(
                centro),
            telefono=self.map_telefono_establecimiento_sanitario(centro),
            descripcion=self.map_descripcion_establecimiento_sanitario(centro),
            en_localidad=localidad
        )
        # print(centro)
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
