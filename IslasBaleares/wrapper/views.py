import os
from IslasBaleares.settings import MEDIA_ROOT
import xmltodict
import json
from django.http import JsonResponse


def cargar_xml(request):
    # Si a la petición GET se añade el parámetro 'all' a true se cargará el fichero con todos los registros
    if request.GET.get('all', False) == 'true':
        path = 'biblioteques.xml'
    # Cargar únicamente únicamente los de la demo
    else:
        path = 'establecimientos-sanitarios-IB.xml'
    # abrir con encoding utf8 para las tildes
    with open(os.path.join(MEDIA_ROOT, path), 'r', encoding='utf-8') as file:
        # parsear a xml
        xmldict = xmltodict.parse(file.read())
        # transformar de xml a json
        xmlJson = json.dumps(xmldict, ensure_ascii=False)
        json_object = json.loads(xmlJson)
        # devolver como json
        return JsonResponse(json_object['response']['row']['row'], safe=False)
