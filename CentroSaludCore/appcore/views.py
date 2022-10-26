from django.http import HttpResponse

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