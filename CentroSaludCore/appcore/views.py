from django.http import HttpResponse
from .extractors import csv_extractor
from .extractors import json_extractor
from .extractors import xml_extractor
from .models import *

# Create your views here.

def cargar_json(request):
    json_extractor.handle_file()
    return HttpResponse(status=200)

def cargar_xml(request):
    xml_extractor.handle_file()
    return HttpResponse(status=200)

def cargar_csv(request):
    csv_extractor.handle_file()
    return HttpResponse(status=200)

def borrar_bdd(request):
    Establecimiento_Sanitario.objects.all().delete()
    Provincia.objects.all().delete()
    Localidad.objects.all().delete()
    return HttpResponse(status=200)