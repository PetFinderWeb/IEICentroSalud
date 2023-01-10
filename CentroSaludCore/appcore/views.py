from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from .extractors.csv_extractor import CSV_Extractor
from .extractors.json_extractor import JSON_Extractor
from .extractors.xml_extractor import XML_Extactor
from .models import *

""" GET. Al ejecutarse elimina todos los registros de la base de datos"""


def borrar_bdd(request):
    if request.GET:
        Establecimiento_Sanitario.establecimientos.all().delete()
        Provincia.objects.all().delete()
        Localidad.objects.all().delete()
        return HttpResponse(status=200)


""" GET. Endpoint para cargar en el warehouse los datos que desee el usuario. Llama a los extractores correspondientes"""


def carga_parametrizada(request):
    errores = []
    centrosSanitarios = 0
    # Comprueba si se ha solicitado cargar los datos del país vasco
    if request.GET.get('p', False) == 'true':
        try:
            extractor = JSON_Extractor()
            # Llamar al extractor del país vasco
            extractor.extraer_datos(
                port=10001, path='/wrapper/cargar_json/')
        except Exception as e:
            # anotamos los errores que se hayan producido en la carga
            errores += [str(e)]
        finally:
            # anotamos los errores que se hayan producido en la carga
            errores += extractor.errores
        # anotamos el número de centros sanitarios añadidos al warehouse
        centrosSanitarios += extractor.centrosSantinarios
    # Comprueba si se ha solicitado cargar los datos de la comunidad valenciana
    if request.GET.get('c', False) == 'true':
        try:
            extractor = CSV_Extractor()
            # Llamar al extractor de la comunidad valenciana
            extractor.extraer_datos(
                port=10000, path='/wrapper/cargar_csv/')
        except Exception as e:
            # anotamos los errores que se hayan producido en la carga
            errores += [str(e)]
        finally:
            # anotamos los errores que se hayan producido en la carga
            errores += extractor.errores
        # anotamos el número de centros sanitarios añadidos al warehouse
        centrosSanitarios += extractor.centrosSantinarios
    # Comprueba si se ha solicitado cargar los datos de las islas baleares
    if request.GET.get('b', False) == 'true':
        try:
            extractor = XML_Extactor()
            # Llamar al extractor de la islas baleares
            extractor.extraer_datos(
                port=10002, path='/wrapper/cargar_xml/')
        except Exception as e:
            # anotamos los errores que se hayan producido en la carga
            errores += [str(e)]
        finally:
            # anotamos los errores que se hayan producido en la carga
            errores += extractor.errores
        # anotamos el número de centros sanitarios añadidos al warehouse
        centrosSanitarios += extractor.centrosSantinarios
    # Devolver en JSON los errores durante la carga y el número de centros sanitarios añadidos
    return JsonResponse(data={'errores': errores, 'centrosSanitarios': centrosSanitarios})


""" GET. Endpoint para buscar en el warehouse los datos que desee el usuario """


def busqueda(request):
    # Recoger los parámetros que el usuario haya introducido en la búsqueda
    localidad = request.GET.get('localidad', '')
    cod_postal = request.GET.get('cod_postal', '')
    provincia = request.GET.get('provincia', '')
    tipo = request.GET.get('tipo', 'T')

    # Filtrar los datos según los parámetros de búsqueda
    queryset = Establecimiento_Sanitario.establecimientos.buscar_por_tipo(
        tipo, provincia, cod_postal, localidad)
    # Serializar el resultado a JSON
    data = serializers.serialize(
        'json', queryset, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')
