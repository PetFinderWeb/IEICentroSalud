from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

from .extractors.csv_extractor import CSV_Extractor
from .extractors.json_extractor import JSON_Extractor
from .extractors.xml_extractor import XML_Extactor
from .models import *

# Create your views here.


def cargar_json(request):
    extractor = JSON_Extractor()
    extractor.extraer_de_fichero()
    return HttpResponse(status=200)


def cargar_xml(request):
    extractor = XML_Extactor()
    extractor.extraer_de_fichero()
    return HttpResponse(status=200)


def cargar_csv(request):
    extractor = CSV_Extractor()
    extractor.extraer_de_fichero()
    return HttpResponse(status=200)


def borrar_bdd(request):
    Establecimiento_Sanitario.objects.all().delete()
    Provincia.objects.all().delete()
    Localidad.objects.all().delete()
    return HttpResponse(status=200)


def carga_parametrizada(request):
    if request.GET.get('p', False) == 'true':
        extractor = JSON_Extractor()
        extractor.extraer_de_fichero()
    if request.GET.get('c', False) == 'true':
        extractor = CSV_Extractor()
        extractor.extraer_de_fichero()
    if request.GET.get('b', False) == 'true':
        extractor = XML_Extactor()
        extractor.extraer_de_fichero()

    return HttpResponse(status=200)


def busqueda(request):
    localidad = request.GET.get('localidad', '')
    cod_postal = request.GET.get('cod_postal', '')
    provincia = request.GET.get('provincia', '')
    tipo = request.GET.get('tipo', 'T')

    queryset = Establecimiento_Sanitario.establecimientos.buscar_por_tipo(
        tipo, provincia, cod_postal, localidad)
    data = serializers.serialize('json', queryset, use_natural_foreign_keys=True)
    return HttpResponse(data, content_type='application/json')
