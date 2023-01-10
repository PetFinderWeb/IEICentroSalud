
from typing import *
from ..models import Establecimiento_Sanitario, Provincia, Localidad
from abc import ABC, abstractmethod
import http.client
import json

""" Clase que representa el extractor de nuestra aplicación. 
    Implementa el patrón Plantilla, de modo que esta clase implementa una serie de métodos 
    comunes e idénticos para los tres extractores (país vasco, comunidad valenciana e islas baleares)
    y define como abstractos otros métodos que son comunes pero que su implementación variará en cada
    extractor, de modo que tienen que ser redefinidos por las clases que deriven de esta."""


class Extractor(ABC):
    # Errores producidos durante la carga en el warehouse
    errores: List[str] = []
    # Número de centros sanitarios añadidos
    centrosSantinarios: int = 0

    # Método plantilla. Se encarga de llamar al wrapper y procesar los datos recibidos por el wrapper
    def extraer_datos(self, port, path, server='localhost', all=False) -> List[str]:
        datos = self.llamar_wrapper(port, path, server, all)
        self.guardar_datos(datos)

    # Método que se encarga de hacer una petición HTTP a un wrapper para obtener los datos de un dataset.
    # Funciona para todos los wrappers ya que recibe por parámetro IP, puerto, ruta relativa al endpoint,
    # y si se todos los datos o solo los de la demo.
    def llamar_wrapper(self, port, path, server, all):
        try:
            # Establece conexión con el wrapper
            connection = http.client.HTTPConnection(server, port)
            # Si se desean todos los datos del wrapper añadir cabecera
            if all == True:
                headers = {"all": "true"}
            else:
                headers = {}
            # Petición GET al endpoint del wrapper
            connection.request("GET", path, headers=headers)
            response = connection.getresponse()
            if response.status != 200:
                raise Exception(
                    "Status code " + str(response.status))
            # Recoger los datos devueltos y decodearlos como utf8 para que funcionen tildes, eñes...
            string = response.read().decode('utf-8')
            json_content = json.loads(string)
            connection.close()
        except Exception as e:
            raise Exception("Error al comunicarse con el wrapper. " + str(e))
        return json_content

    # Método que se ejecuta una vez se ha llamado al wrapper, se encarga de llamar a los métodos que
    # almacenan provincia, localidad y centro sanitario. Se encarga también de recoger los errores durante
    # la carga y anotar el número de centros sanitarios añadidos.
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

    # Método que se encarga de almacenar una provincia en la base de datos si no existe aún.
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

    # Método que se encarga de almacenar una localidad en la base de datos si no existe aún.
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
        # Comprobamos si el centro ya existe en la base de datos por su nombre
        centroRepetido = Establecimiento_Sanitario.establecimientos.filter(
            nombre__iexact=nombre
        )
        if centroRepetido.count() != 0:
            raise Exception("El centro sanitario " +
                            nombre + " se encuentra repetido.")
        # Llama a los métodos que se encargan de realizar los mappings. Estos métodos deberán ser
        # redefinidos por los extractores que extiendan de esta clase pues son métodos abstractos
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
        # Almacenar en la base de datos el centro
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
