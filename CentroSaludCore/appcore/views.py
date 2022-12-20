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
    query_set = Establecimiento_Sanitario.objects.all()
    query_provincia = Establecimiento_Sanitario.objects.none()    
    query_localidades = Establecimiento_Sanitario.objects.none()    
    query_cod_postal = Establecimiento_Sanitario.objects.none()
    query_tipo = Establecimiento_Sanitario.objects.none()

    if localidad != "":
        query_localidades = query_set.filter(en_localidad__nombre=localidad)
    if cod_postal != "":
        query_cod_postal = query_set.filter(codigo_postal=cod_postal)
    if provincia != "":
        query_provincia = query_set.filter(en_localidad__en_provincia__nombre=provincia)
        print(query_provincia)
    if tipo != 'T':
        query_tipo = query_set.filter(tipo=tipo)
        
    query_final = query_localidades.union(query_cod_postal).union(query_provincia).intersection(query_tipo)
    
    return HttpResponse(status=200)