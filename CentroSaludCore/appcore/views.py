from django.http import HttpResponse
from CentroSaludCore.settings import MEDIA_ROOT
from extractors import csv_extractor
from extractors import json_extractor
from extractors import xml_extractor

# Create your views here.

def cargar_json(request):
    with open(MEDIA_ROOT + '/bibliotecas.json') as file:
        json_extractor.handlefile(file)
        return HttpResponse(status=200)

def cargar_xml(request):
    with open(MEDIA_ROOT + '/biblioteques.xml') as file:
        xml_extractor.handlefile(file)
        return HttpResponse(status=200)

def cargar_csv(request):
    with open(MEDIA_ROOT + '/directorio-de-bibliotecas-valencianas_2020.csv') as file:
        csv_extractor.handlefile(file)
        return HttpResponse(status=200)