import os
from IslasBaleares.settings import MEDIA_ROOT
import xmltodict
import json
from django.http import JsonResponse


def cargar_xml(request):
    # Cargar todos los registros o únicamente los de la demo
    if request.GET.get('all', False) == 'true':
        path = 'biblioteques.xml'
    else:
        path = 'establecimientos-sanitarios-IB.xml'
    # abrir con encoding utf8 para las tildes
    with open(os.path.join(MEDIA_ROOT, path), 'r', encoding='utf-8') as file:
        # parsear a xml
        xmldict = xmltodict.parse(file.read())
        # parsear a json
        xmlJson = json.dumps(xmldict, ensure_ascii=False)
        json_object = json.loads(xmlJson)
        # devolver como json
        return JsonResponse(json_object['response']['row']['row'], safe=False)
